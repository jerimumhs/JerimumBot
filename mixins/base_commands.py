import logging
import pyowm
from decouple import config

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
        dp.add_handler(CommandHandler("clima", self.__class__.weather, pass_args=True))

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

    @staticmethod
    def weather(bot, update, args):
        """Define weather at certain location"""
        api_key = config('OPENWEATHERMAP_TOKEN')
        owm = pyowm.OWM(api_key)
        text_location = "".join(str(x) for x in args)
        observation = owm.weather_at_place(text_location)
        w = observation.get_weather()
        humidity = w.get_humidity()
        wind = w.get_wind()
        temp = w.get_temperature('celsius')
        convert_temp = temp.get('temp')
        convert_wind = wind.get('speed')
        convert_humidity = humidity
        text_temp = str(convert_temp)
        text_wind = str(convert_wind)
        text_humidity = str(convert_humidity)
        update.message.reply_text("O clima hoje em {} está: \n"
                                  "🌡 Temperatura: {} celsius \n"
                                  "💨 Velocidade do Vento: {} m/s \n"
                                  "💧 Humidade: {}%".format(text_location, text_temp, text_wind, text_humidity))
