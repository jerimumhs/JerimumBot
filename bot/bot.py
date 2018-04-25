from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters, CallbackQueryHandler)
import logging
from pymongo import MongoClient

from . import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

cliente = MongoClient('localhost', 27017)
banco = cliente['JerimumHSBot']
mensagens = banco['mensagens']


def load_messages(group_id, message):
    custom = mensagens.find_one({"_id": group_id})
    if custom and custom.get(message):
        return custom[message]
    default = mensagens.find_one({"_id": "default"})
    return default[message]

def start(bot, update):
    """Send a message when the command /start is issued."""
    start = (load_messages(
        update.message.chat_id, "start"))
    update.message.reply_text(start)


def help(bot, update):
    """Send a message when the command /help is issued."""
    help = (load_messages(
        update.message.chat_id, "help"))
    update.message.reply_text(help)


def welcome(bot, update):
    """Send a message when a new user join the group."""
    welcome = (load_messages(
        update.message.chat_id, "welcome")).format(
            full_name=update.message.new_chat_members[0].full_name)
    
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
    update.message.reply_text(welcome, reply_markup=reply_markup)


def button(bot, update):
    query = update.callback_query
    
    if query.data == "rules":
        bot.answer_callback_query(
            callback_query_id=query.id,
            text=(
                (load_messages(
                    update.message.chat_id, "rules_bit"))
            ),
            show_alert=True
        )
    elif query.data == "site":
       bot.answer_callback_query(
           callback_query_id=query.id
       )

def bye(bot, update):
    """Send a message when a user leaves the group."""
    bye = (load_messages(
            update.message.chat_id, "bye")).format(
                full_name=update.message.left_chat_member.full_name)
    update.message.reply_text(bye)

def rules(bot, update):
    """Send a message with the group rules."""
    rules = (load_messages(
        update.message.chat_id, "rules_complete"))
    if adm_verify(update):
        update.message.reply_text(rules)
    else:        
        bot.sendMessage(
            chat_id=update.message.from_user.id, 
            text=rules)


def description(bot, update):
    """Send a message with the group description."""
    description = (load_messages(
        update.message.chat_id, "description"))
    if adm_verify(update):
        update.message.reply_text(description)
    else:        
        bot.sendMessage(
            chat_id=update.message.from_user.id, 
            text=description)


def xinga(bot, update):
    """Send the Guilherme picture."""
    bot.send_sticker(sticker="CAADAQADCgEAAmOWFQq4zU4TMS08AwI",
                     chat_id=update.message.chat_id)


def error(bot, update, error):
    """Log Errors caused by Updates."""
    if error.message == "Forbidden: bot can't initiate conversation with a user":
        update.message.reply_text(
            "Por favor, inicie uma conversa comigo para que eu possa te enviar uma mensagem!")
    elif error.message == "Forbidden: bot was blocked by the user":
        update.message.reply_text(
            "Você me bloqueou?! Tsc tsc. Que feio!!!🙄")
    else:
        logger.warning('Update "%s" caused error "%s"', update, error)

def adm_verify(update):
    if update.message.chat.get_member(update.message.from_user.id).status in ('creator', 'administrator'):
        return True
    return False


def run_bot():
    """Start the bot."""
    updater = Updater(config['telegram']['token'])

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("ajuda", help))
    dp.add_handler(CommandHandler("regras", rules))
    dp.add_handler(CommandHandler("xinga", xinga))
    dp.add_handler(CommandHandler("descricao", description))

    dp.add_handler(MessageHandler(
        Filters.status_update.new_chat_members, welcome))

    dp.add_handler(MessageHandler(
        Filters.status_update.left_chat_member, bye))

    dp.add_handler(CallbackQueryHandler(button))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()
