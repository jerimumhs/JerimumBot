import logging
import random
import re
import datetime

from bs4 import BeautifulSoup
import requests
from telegram.ext import CommandHandler

from core import BotTelegramCore

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO)

logger = logging.getLogger(__name__)

last_call = None
QTY_POSTS_PER_PAGE = 20


def coach(bot, update, args):
    global last_call
    last_call = last_call
    actual_call = datetime.datetime.now()

    url_base = 'https://www.pensador.com'

    if len(args) == 0:
        query = "motivacional/"
        url_search = f'{url_base}/{query}/'
    else:
        pre_query = "+".join(args)
        query = f'busca.php?q={pre_query}/'
        url_search = f'{url_base}/{query}&p='

    if not last_call:
        last_call = actual_call

    diff_seconds = (actual_call - last_call).seconds

    if last_call == actual_call or diff_seconds > 300:
        last_call = datetime.datetime.now()
        response = requests.get(url_search)

        soup = BeautifulSoup(response.content, 'html.parser')
        tag_total = soup.find(class_='total')
        if tag_total is None:
            update.message.reply_text(
                "Desculpe, ainda não conheço nada sobre o assunto.")

        text_total = tag_total.get_text()
        total_match = re.search(r"\d+", text_total)
        string_total = total_match.group(0)

        total_pages = int(string_total) // QTY_POSTS_PER_PAGE

        random_page = random.randint(1, total_pages)
        response_two = requests.get(f'{url_search}{random_page}')

        soup_two = BeautifulSoup(response_two.content, 'html.parser')
        frases = soup_two.find_all(class_='fr')

        update.message.reply_text(
            frases[random.randint(0, len(frases) - 1)].get_text())
        return

    update.message.reply_text(
        "TIMEOUT_COACH: O filhão, se quiser mais por enquanto vai"
        "ter que fazer meu curso pago de coach quântico"
        "e reprogramador de DNA!")


def config_handlers(instance: BotTelegramCore):
    logging.info('Configurando comandos de coach quantico do bot...')

    instance.updater.dispatcher.add_handler(
        CommandHandler("coach", coach, pass_args=True))
