import logging

from telegram.ext import CallbackQueryHandler

from core import BotTelegramCore
from messages import RULES_BIT


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def handle_callback(bot, update):
    query = update.callback_query

    if query.data == "rules":
        bot.answer_callback_query(
            callback_query_id=query.id,
            text=RULES_BIT,
            show_alert=True
        )
    elif query.data == "site":
        bot.answer_callback_query(
            callback_query_id=query.id
        )


def config_handlers(instance: BotTelegramCore):
    logging.info('Configurando callback handler do bot...')

    instance.add_handler(
        CallbackQueryHandler(handle_callback)
    )
