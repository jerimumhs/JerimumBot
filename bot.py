import logging

from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (Updater, CommandHandler,
                          MessageHandler, Filters, CallbackQueryHandler)

from messages import (START, HELP, BYE, DESCRIPTION,
                      WELCOME, RULES_COMPLETE, RULES_BIT,
                      ERROR_BLOCKED, ERROR_INITIATE)

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


class JerimumBot(object):
    def __init__(self, token, port, heroku_app_name):
        logging.info('Inicializando o bot...')
        self.token = token
        self.port = port
        self.heroku_app_name = heroku_app_name

        self.updater = Updater(self.token)
        self.config_handlers()

    def config_handlers(self):
        logging.info('Configurando comandos do bot...')
        dp = self.updater.dispatcher

        dp.add_handler(CommandHandler("regras", JerimumBot.rules))
        dp.add_handler(CommandHandler("descricao", JerimumBot.description))

        dp.add_handler(CommandHandler("start", lambda bot, update: update.message.reply_text(START)))
        dp.add_handler(CommandHandler("ajuda", lambda bot, update: update.message.reply_text(HELP)))
        dp.add_handler(CommandHandler("xinga", lambda bot, update: bot.send_sticker(
            sticker="CAADAQADCgEAAmOWFQq4zU4TMS08AwI",
            chat_id=update.message.chat_id)))

        dp.add_handler(MessageHandler(
            Filters.status_update.new_chat_members, JerimumBot.welcome))

        dp.add_handler(MessageHandler(
            Filters.status_update.left_chat_member,
            lambda bot, update: update.message.reply_text(
                BYE.format(full_name=update.message.left_chat_member.full_name))))

        dp.add_handler(CallbackQueryHandler(JerimumBot.button))

        dp.add_error_handler(JerimumBot.error)

    def run_web(self):
        """Start the bot."""

        self.updater.start_webhook(
            listen="0.0.0.0",
            port=self.port,
            url_path=self.token
        )

        self.updater.bot.set_webhook(f"https://{self.heroku_app_name}.herokuapp.com/{self.token}")

        logging.info('Bot está rodando!')
        self.updater.idle()

    def run_cmd(self):
        self.updater.start_polling()

        logging.info('Bot está rodando!')
        self.updater.idle()

    def run(self, mode='cmd'):
        if mode == 'cmd':
            self.run_cmd()
        elif mode == 'web':
            self.run_web()
        else:
            raise Exception('O modo passado não foi reconhecido')

    @staticmethod
    def description(bot, update):
        """Send a message with the group description."""
        if JerimumBot.adm_verify(update):
            update.message.reply_text(DESCRIPTION)
        else:
            bot.sendMessage(
                chat_id=update.message.from_user.id,
                text=DESCRIPTION)

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

    @staticmethod
    def rules(bot, update):
        """Send a message with the group rules."""
        if JerimumBot.adm_verify(update):
            update.message.reply_text(RULES_COMPLETE)
        else:
            bot.sendMessage(
                chat_id=update.message.from_user.id,
                text=RULES_COMPLETE)

    @staticmethod
    def error(bot, update, err):
        """Log Errors caused by Updates."""
        if err.message == "Forbidden: bot can't initiate conversation with a user":
            update.message.reply_text(ERROR_INITIATE)
        elif err.message == "Forbidden: bot was blocked by the user":
            update.message.reply_text(ERROR_BLOCKED)
        else:
            logger.warning('Update "%s" caused error "%s"', update, err)

    @staticmethod
    def button(bot, update):
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

    @staticmethod
    def adm_verify(update):
        return update.message.chat.get_member(update.message.from_user.id).status in ('creator', 'administrator')
