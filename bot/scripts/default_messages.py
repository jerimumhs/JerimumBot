from pymongo import MongoClient

cliente = MongoClient('localhost', 27017)
banco = cliente['JerimumHSBot']
mensagens = banco['mensagens']

regras_completo = (
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

regras_resumo = (
    "REGRAS:\n\n"
    "1.Respeitar os membros do grupo\n"
    "2.Não compartilhar conteúdo sem autorização\n"
    "3.Não enviar Spam\n"
    "4.Proibido envio de material pornográfico\n"
    "5.Havendo qualquer restrição às regras, será banido"
)

description = (
    "O Jerimum Hackerspace é um local aberto e colaborativo que "
    "fomenta a troca de conhecimento e experiências, onde as pessoas "
    "podem se encontrar, socializar, compartilhar e colaborar. "
    "Também onde entusiastas de tecnologia realizem projetos em "
    "diversas áreas, como segurança, hardware, eletrônica, robótica, "
    "espaçomodelismo, software, biologia, música, artes plásticas "
    "ou o que mais a criatividade permitir."
)

boas_vindas = (
    "Olá {full_name}, seja bem-vindo ao Jerimum Hackerspace\n\n"
    "Somos um grupo de pessoas interessadas em usar, remixar e compartilhar "
    "tecnologia, aprendizado, diversão e cultura de forma colaborativa e indiscriminada.\n\n"
    "Leia nossas /regras e agora porque você não fala um pouco sobre você?"
)

despedida = (
    "{full_name} acabou de sair do grupo, uma palminha, e uma vainha...\n\n"
    "UUUuuuUUuUUUuUUUuu"
)

mensagens.insert_one({
    "_id": "default",
        "regras_completo": regras_completo,
        "regras_resumo": regras_resumo,
        "description": description,
        "boas_vindas": boas_vindas,
        "despedida": despedida
    })

