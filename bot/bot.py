from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging

from . import config

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Para começar, basta digitar!')


def help(bot, update):
    """Send a message when the command /help is issued."""
    help = (
        "Está com duvidas? Fale com nossos membros!\n"
        "Em caso de duvidas mais especificas procure nossos Administradores."
    )
    update.message.reply_text(help)


def welcome(bot, update):
    """Send a message when a new user join the group."""
    welcome = (
        "Olá {first_name}, seja bem-vindo ao Jerimum Hackerspace\n\n"
        "Somos um grupo de pessoas interessadas em usar, remixar e compartilhar "
        "tecnologia, aprendizado, diversão e cultura de forma colaborativa e indiscriminada.\n\n"
        "Leia nossas /regras e agora porque você não fala um pouco sobre você?"
    ).format(first_name=update.message.new_chat_members[0].full_name)
    update.message.reply_text(welcome)


def bye(bot, update):
    """Send a message when a user leaves the group."""
    bye = (
        "{first_name} acabou de sair do grupo, uma palminha, e uma vainha...\n\n"
        "UUUuuuUUuUUUuUUUuu"
    ).format(first_name=update.message.left_chat_member.full_name)
    update.message.reply_text(bye)

def rules(bot, update):
    """Send a message with the group rules."""
    rules = (
        "1. Não haver discriminação em nenhum sentido, raça, religião, "
        "sexo ou linguagem de programação.\n"
        "2. Esse não é um grupo para discussões de política ou religião, "
        "existe lugares para isso, mas não é aqui.\n"
        "3. Evite mensagens religiosas, não somos contra religião, só "
        "que esse grupo tem foco claro. \n"
        "4. Evite postagens de cunho comercial, venda de produtos e "
        "serviços, e outros tipos de ações correlacionadas. Não é "
        "proibido, mas peça permissão aos administradores antes.\n"
        "5. Não compartilhar conteúdo sem autorização ou que a licença"
        " permita. \n"
        "6. Proibido envio de vídeos ou imagens pornográficas, acidentes, "
        "informações que não sejam de carácter tecnológico. \n"
        "7. Não ficar fazendo flood conversando com o Guilherme_Bot.\n"
        "8. Encontrou alguma mensagens em desacordo com nossas regras, "
        "por favor avise nossos administradores.\n"
        "9. Havendo qualquer restrição as regras será banido. \n\n"
        "Att. Jerimum Hacker Bot <3"
        )
    if update.message.chat.get_member(update.message.from_user.id).status in ('creator', 'administrator'):
        update.message.reply_text(rules)
    else:
        bot.sendMessage(chat_id=update.message.from_user.id, text=rules)


def description(bot, update):
    """Send a message with the group description."""
    description = (
        "O Jerimum Hackerspace é um local aberto e colaborativo que "
        "fomenta a troca de conhecimento e experiências, onde as pessoas "
        "podem se encontrar, socializar, compartilhar e colaborar. "
        "Também onde entusiastas de tecnologia realizem projetos em "
        "diversas áreas, como segurança, hardware, eletrônica, robótica, "
        "espaçomodelismo, software, biologia, música, artes plásticas "
        "ou o que mais a criatividade permitir."
    )
    if update.message.chat.get_member(update.message.from_user.id).status in ('creator', 'administrator'):
        update.message.reply_text(description)
    else:
        bot.sendMessage(chat_id=update.message.from_user.id, text=description)


def xinga(bot, update):
    """Send the Guilherme picture."""
    bot.send_photo(chat_id=update.message.chat_id,
                   photo=open('bot/imgs/guilherme.jpg', 'rb'),
                   caption="Guilherme presente!")


def error(bot, update, error):
    """Log Errors caused by Updates."""
    if error.message == "Forbidden: bot can't initiate conversation with a user":
        update.message.reply_text(
            "Por favor, inicie uma conversa comigo para que eu possa te enviar as regras!")
    logger.warning('Update "%s" caused error "%s"', update, error)


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

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()
