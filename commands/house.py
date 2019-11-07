import logging

from telegram.ext import (CommandHandler)

from db import Status
from core import BotTelegramCore
from messages import UNAUTHORIZED, I_DONT_KNOW


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def aberta(bot, update):
    """Set the status of our home as open and send referring sticker."""
    user_id = update.message.from_user.id
    if BotTelegramCore.is_admin(user_id):
        _status = Status.aberta(user_id)
        bot.send_sticker(
            sticker=_status.sticker,
            chat_id=BotTelegramCore.instance().chat_id)
    else:
        update.message.reply_text(UNAUTHORIZED)


def fechada(bot, update):
    """Set the status of our home as closed and send referring sticker."""
    user_id = update.message.from_user.id
    if BotTelegramCore.is_admin(user_id):
        _status = Status.fechada(user_id)
        bot.send_sticker(
            sticker=_status.sticker,
            chat_id=BotTelegramCore.instance().chat_id)
    else:
        update.message.reply_text(UNAUTHORIZED)


def status(bot, update):
    """Send a sticker or message with the status of our home."""
    _status = Status.now()
    if _status is not None:
        bot.send_sticker(
            sticker=Status.now().sticker,
            chat_id=BotTelegramCore.instance().chat_id)
    else:
        update.message.reply_text(I_DONT_KNOW)


def config_handlers(instance: BotTelegramCore):
    logging.info('Configurando comandos de casa do bot...')

    instance.add_handler(
        CommandHandler("aberta", aberta))

    instance.add_handler(
        CommandHandler("fechada", fechada))

    instance.add_handler(
        CommandHandler("status", status))
