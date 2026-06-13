from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def start_keyboard() -> InlineKeyboardMarkup:
    buttons = [
        [InlineKeyboardButton("📚 Horário de Banco de Dados", callback_data="horario banco de dados")],
        [InlineKeyboardButton("📍 Onde fica o Lab 1?", callback_data="onde fica o lab 1")],
        [InlineKeyboardButton("📞 Contato da Coordenação", callback_data="contato coordenação")],
        [InlineKeyboardButton("🍽️ Horário do RU", callback_data="horário do RU")],
    ]
    return InlineKeyboardMarkup(buttons)
