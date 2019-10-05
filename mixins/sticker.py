import logging

from telegram.ext import (CommandHandler)

from core import BotTelegramCore


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class StickerBotMixin(BotTelegramCore):
    def config_handlers(self):
        logging.info('Configurando comandos de sticker do bot...')

        self.updater.dispatcher.add_handler(CommandHandler("xinga", lambda bot, update: bot.send_sticker(
            sticker="CAADAQADCgEAAmOWFQq4zU4TMS08AwI",
            chat_id=update.message.chat_id)))
