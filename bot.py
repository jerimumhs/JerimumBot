from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    update.message.reply_text("Olá")

def help(bot, update):
    update.message.reply_text("Ajuda")

def main():
    updater = Updater("522838006:AAEwzvOE8aePKgmNxzn3w88Bmub5jkStYKs")

    dp = updater.dispatcher

    dp = add_handler(CommandHandler("start", start))
    dp = add_handler(CommandHandler("help", help))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    update.start_polling()

    update.idle()

    if __name__ == '__main__':
        main()