import logging

from telegram.ext import CommandHandler

from core import BotTelegramCore, adm_verify
from messages import START, HELP, DESCRIPTION, RULES_COMPLETE


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class BaseCommandsBotMixin(BotTelegramCore):
    def config_handlers(self):
        logging.info('Configurando comandos base do bot...')
        dp = self.updater.dispatcher

        dp.add_handler(CommandHandler("regras", self.__class__.rules))
        dp.add_handler(CommandHandler("descricao", self.__class__.description))

        dp.add_handler(CommandHandler("start", lambda bot, update: update.message.reply_text(START)))
        dp.add_handler(CommandHandler("ajuda", lambda bot, update: update.message.reply_text(HELP)))

    @staticmethod
    def description(bot, update):
        """Send a message with the group description."""
        if adm_verify(update):
            update.message.reply_text(DESCRIPTION)
        else:
            bot.sendMessage(
                chat_id=update.message.from_user.id,
                text=DESCRIPTION)

    @staticmethod
    def rules(bot, update):
        """Send a message with the group rules."""
        if adm_verify(update):
            update.message.reply_text(RULES_COMPLETE)
        else:
            bot.sendMessage(
                chat_id=update.message.from_user.id,
                text=RULES_COMPLETE)
