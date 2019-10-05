import logging
import random
import re
import time
import urllib.request

from bs4 import BeautifulSoup
import requests
from telegram.ext import CommandHandler

from core import BotTelegramCore

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def coach(bot, update):
    """Manda uma mensagem motivacional"""
    url_base = 'https://www.pensador.com/motivacional/'
    response = requests.get(url_base)

    soup = BeautifulSoup(response.content, 'html.parser')
    tag_total = soup.find(class_='total')

    text_total = tag_total.get_text()
    total_match = re.search(r"\d+", text_total)
    string_total = total_match.group(0)

    total_pages = int(string_total) // 20

    random_page = random.randint(2, total_pages)
    url_search = f'{url_base}{random_page}/'
    response_two = requests.get(url_search)

    soup_two = BeautifulSoup(response_two.content, 'html.parser')
    frases = soup_two.find_all(class_='fr')

    update.message.reply_text(frases[random.randint(0,len(frases))].get_text())

def config_handlers(instance: BotTelegramCore):
    logging.info('Configurando comandos de coach quantico do bot...')

    instance.updater.dispatcher.add_handler(CommandHandler("coach", coach))
