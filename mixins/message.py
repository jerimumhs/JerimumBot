import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, Filters

from core import BotTelegramCore
from messages import BYE, WELCOME


logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class MessageBotMixin(BotTelegramCore):
    def config_handlers(self):
        logging.info('Configurando message handlers do bot...')

        self.updater.dispatcher.add_handler(MessageHandler(
            Filters.status_update.new_chat_members, self.__class__.welcome))

        self.updater.dispatcher.add_handler(MessageHandler(
            Filters.status_update.left_chat_member,
            lambda bot, update: update.message.reply_text(
                BYE.format(full_name=update.message.left_chat_member.full_name))))

    @staticmethod
    def welcome(bot, update):
        """Send a message when a new user join the group."""
        welcome_message = WELCOME.format(full_name=update.message.new_chat_members[0].full_name)

        keyboard = [
            [
                InlineKeyboardButton(
                    "Resumo das regras!",
                    callback_data='rules')
            ],

            [
                InlineKeyboardButton(
                    "Nosso site!",
                    callback_data='site',
                    url="http://www.jerimumhs.org/"),

                InlineKeyboardButton(
                    "Nosso Facebook!",
                    callback_data='site',
                    url="https://www.facebook.com/JerimumHS/")
            ],

            [
                InlineKeyboardButton(
                    "Nosso GitHub!",
                    callback_data='site',
                    url="https://github.com/jerimumhs/")
            ]
        ]

        reply_markup = InlineKeyboardMarkup(keyboard)
        update.message.reply_text(welcome_message, reply_markup=reply_markup)
