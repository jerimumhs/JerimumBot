import logging
import pyowm

from pyowm.exceptions.api_response_error import NotFoundError
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
        text_location = " ".join(args)
        try:
            observation = owm.weather_at_place(text_location)
        except NotFoundError:
            update.message.reply_text(f"⚠️ Não consegui localizar a cidade {text_location}!")
        weather = observation.get_weather()
        humidity = weather.get_humidity()
        wind = weather.get_wind()
        temp = weather.get_temperature('celsius')
        update.message.reply_text(f"🧭 Localização: {text_location}\n"
                                  f"🔥️ Temperatura Maxima: {temp.get('temp_max')} celsius \n"
                                  f"❄️ Temparatura Minima: {temp.get('temp_min')} celsius\n"
                                  f"💨 Velocidade do Vento: {wind.get('speed')} m/s \n"
                                  f"💧 Humidade: {humidity}%")
