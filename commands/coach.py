import logging
import random
import re

from bs4 import BeautifulSoup
import requests
from telegram.ext import CommandHandler

from core import BotTelegramCore
from db import CommandCall
from messages import COMMAND_THROTTLED


logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)


QTY_POSTS_PER_PAGE = 20


def coach(bot, update, args):
    user = update.message.from_user
    bot_instance = BotTelegramCore.instance()

    if bot_instance.is_from_oficial_chat(update):
        if not CommandCall.allow_call(command=CommandCall.COACH):
            last_call = CommandCall.last_coach()
            bot.sendMessage(
                chat_id=user.id,
                text=COMMAND_THROTTLED.format(
                    segundos=last_call.cooldown_left,
                    comando=last_call.value))
            return

    url_base = 'https://www.pensador.com'

    if len(args) == 0:
        query = "motivacional/"
        url_search = f'{url_base}/{query}/'
    else:
        pre_query = "+".join(args)
        query = f'busca.php?q={pre_query}/'
        url_search = f'{url_base}/{query}&p='

    response = requests.get(url_search, timeout=1)

    soup = BeautifulSoup(response.content, 'html.parser')
    tag_total = soup.find(class_='total')
    if tag_total is None:
        update.message.reply_text(
            "Desculpe, ainda não conheço nada sobre o assunto.")

    text_total = tag_total.get_text()
    total_match = re.search(r"\d+", text_total)
    string_total = total_match.group(0)

    total_pages = int(string_total) // QTY_POSTS_PER_PAGE or 1

    random_page = random.randint(1, total_pages)
    response_two = requests.get(f'{url_search}{random_page}', timeout=1)

    soup_two = BeautifulSoup(response_two.content, 'html.parser')
    frases = soup_two.find_all(class_='fr')

    update.message.reply_text(
        frases[random.randint(0, len(frases) - 1)].get_text())

    if bot_instance.is_from_oficial_chat(update):
        CommandCall.coach(user.username)


def config_handlers(instance: BotTelegramCore):
    logging.info('Configurando comandos de coach quantico do bot...')

    instance.add_handler(
        CommandHandler("coach", coach, pass_args=True))
