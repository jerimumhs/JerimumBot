import logging

from core import BotTelegramCore
from messages import ERROR_BLOCKED, ERROR_INITIATE


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def error(bot, update, err):
    """Log Errors caused by Updates."""
    if err.message == "Forbidden: bot can't initiate conversation with a user":
        update.message.reply_text(ERROR_INITIATE)
    elif err.message == "Forbidden: bot was blocked by the user":
        update.message.reply_text(ERROR_BLOCKED)
    else:
        logger.warning('Update "%s" caused error "%s"', update, err)


def config_handlers(instance: BotTelegramCore):
    logging.info('Configurando error handler do bot...')
    instance.updater.dispatcher.add_error_handler(error)
