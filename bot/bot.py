from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

from . import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def rules(bot, update):
    """Send a message with the group rules."""
    rules = (
        "Amet fufe fit eget nifi auctor nifl nifh ifum luctuf in "
        "fufto malefuada in tinfidunt lafinia auctor fiferra turfif "
        "aliquam eu iaculif malefuada iaculif ifum amet fufto diam "
        "urna fit fehicula turfif auctor eget lectuf luctuf maefenaf "
        "a confectetur lafinia magna magna hafitafe turfif luctuf amet"
        " luctuf efifitur malefuada lorem urna ifum fofuere in eu turfif "
        "efifitur lorem ifum feftifulum fit aliquam fiferra maefenaf turfif "
        "leo mi fit confectetur eu eft luctuf malefuada a faufifuf "
        "tinfidunt nifh et urna aliquam in diam fafien dictumft fufto eget"
        " nifh magna confectetur magna in follifitudin et fofuere euifmod "
        "diam euifmod eft diam confectetur."
        )
    update.message.reply_text(rules)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def run_bot():
    """Start the bot."""
    updater = Updater(config['telegram']['token'])

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("rules", rules))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

