from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

from . import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')


def echo(bot, update):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def rules(bot, update):
    """Send a message with the group rules."""
    rules = (
        "Regras do grupo\n"
        "Pessoal, como em toda boa comunidade, nós precisamos de regras.\n"
        "Tentaremos mantê-las ao mínimo para que seja possível a convivência pacífica.\n"
        "Eventualmente, atualizaremos para uma comunidade melhor desenvolvida.\n\n"
        "Objetivos do grupo:\n\n"
        "1. Manuntenção de um Hackerspace em Natal/RN;\n"
        "2. Desenvolver comunicação entre a comunidade do hackerspace.\n"
        "3. Troca de conhecimento entre os participantes.\n\n"
        "Regras gerais\n\n"
        "1. Não mande correntes, não importa o conteúdo. NÃO ENVIE CORRENTES.\n"
        "2. Esse não é um grupo para discussões de política ou religião, existe lugares para isso, mas não é aqui.\n"
        "3. Evite mensagens religiosas, não somos contra religião, só que esse grupo tem foco claro. \n"
        "4. Evite postagens de cunho comercial, venda de produtos e serviços, e outros tipos de ações "
        "correlacionadas. Não é proibido, mas lembre-se que esse não é o objetivo do grupo.\n"
        "5. Respeite tudo e todos, seja uma pessoa excelente. \n"
        "6. Conforme o grupo cresce, e devido ao grande volume de trabalho fica cada vez mais difícil acompanhar "
        "todas as mensagens, por isso se verificar algum post ou troca de mensagens em desacordo com nossas "
        "regras, por favor avise nossos administradores.\n\n"
        "No entanto é isso.\n"
        "Att. Jerimum Hacker Bot <3"
        )
    update.message.reply_text(rules)


def xinga(bot, update):
    """Send the Guilherme picture."""
    bot.send_photo(chat_id=update.message.chat_id,
                   photo=open('bot/imgs/guilherme.jpg', 'rb'),
                   caption="Guilherme presente!")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)


def run_bot():
    """Start the bot."""
    updater = Updater(config['telegram']['token'])

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("rules", rules))
    dp.add_handler(CommandHandler("xinga", xinga))

    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()

