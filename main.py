import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, CallbackQueryHandler, filters

from src.data.loader import load_data
from src.bot.handlers import start, handle_message, handle_callback

load_dotenv()


def main() -> None:
    data = load_data()

    app = ApplicationBuilder().token(os.environ["TELEGRAM_TOKEN"]).build()
    app.bot_data["ic_data"] = data

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(handle_callback))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    print("Bot running...")
    app.run_polling()


if __name__ == "__main__":
    main()
