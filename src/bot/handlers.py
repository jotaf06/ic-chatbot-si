from telegram import Update
from telegram.constants import ChatAction
from telegram.ext import ContextTypes

from src.ai.llm import parse_intent
from src.data.search import search_discipline, search_location, search_contact
from src.utils.formatter import (
    format_discipline,
    format_location,
    format_contact,
    format_not_found,
    format_unknown,
)
from src.bot.keyboards import start_keyboard

WELCOME_MESSAGE = (
    "👋 Olá! Sou o bot do IC/UFAL.\n\n"
    "Posso te ajudar com:\n"
    "  • Horários e salas de disciplinas\n"
    "  • Localização de laboratórios e setores\n"
    "  • Contatos da coordenação e secretaria\n\n"
    "Me pergunte algo ou escolha uma opção abaixo:"
)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        WELCOME_MESSAGE,
        reply_markup=start_keyboard(),
    )


async def _process(text: str, data: dict, reply_func) -> None:
    parsed = parse_intent(text)
    intent = parsed.get("intent", "unknown")
    term = parsed.get("term", "")

    match intent:
        case "discipline":
            result = search_discipline(data, term)
            reply = format_discipline(result) if result else format_not_found(term)
        case "location":
            result = search_location(data, term)
            reply = format_location(result) if result else format_not_found(term)
        case "contact":
            result = search_contact(data, term)
            reply = format_contact(result) if result else format_not_found(term)
        case _:
            reply = format_unknown()

    await reply_func(reply, parse_mode="Markdown")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await context.bot.send_chat_action(update.effective_chat.id, ChatAction.TYPING)
    await _process(update.message.text, context.bot_data["ic_data"], update.message.reply_text)


async def handle_callback(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    query = update.callback_query
    await query.answer()
    await context.bot.send_chat_action(query.message.chat_id, ChatAction.TYPING)
    await _process(query.data, context.bot_data["ic_data"], query.message.reply_text)
