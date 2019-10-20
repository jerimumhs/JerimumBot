import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup, ParseMode
from telegram.ext import MessageHandler, Filters

from core import BotTelegramCore
from messages import BYE, WELCOME


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


def welcome(bot, update):
    """Send a message when a new user join the group."""
    new_member = update.message.new_chat_members[0]

    welcome_message = WELCOME.format(
        full_name=f'[{new_member.full_name}](tg://user?id={new_member.id})'
    )

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
                url="https://jerimumhacker.space/"),

            InlineKeyboardButton(
                "Apoie-nos!",
                callback_data='site',
                url="https://www.picpay.me/JerimumHS/")
        ],

        [
            InlineKeyboardButton(
                "Nosso GitHub!",
                callback_data='site',
                url="https://github.com/jerimumhs/"),

            InlineKeyboardButton(
                "Nosso Facebook!",
                callback_data='site',
                url="https://www.facebook.com/JerimumHS/")
        ]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text(welcome_message,
                              reply_markup=reply_markup,
                              parse_mode=ParseMode.MARKDOWN)


def config_handlers(instance: BotTelegramCore):
    logging.info('Configurando message handlers do bot...')

    instance.updater.dispatcher.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, welcome))

    instance.updater.dispatcher.add_handler(MessageHandler(
        Filters.status_update.left_chat_member,
        lambda bot, update: update.message.reply_text(
            BYE.format(
                full_name=f'[{update.message.left_chat_member.full_name}]'
                          f'(tg://user?id={update.message.left_chat_member.id})'
            ),
            parse_mode=ParseMode.MARKDOWN
        )
    ))
