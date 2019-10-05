# Jerimum Bot

[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)
![GitHub](https://img.shields.io/github/license/jerimumhs/jerimumbot)
![GitHub language count](https://img.shields.io/github/languages/count/jerimumhs/jerimumbot)
![GitHub top language](https://img.shields.io/github/languages/top/jerimumhs/jerimumbot)
![GitHub issues](https://img.shields.io/github/issues/jerimumhs/jerimumbot)
![GitHub closed issues](https://img.shields.io/github/issues-closed/jerimumhs/jerimumbot)
![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/jerimumhs/jerimumbot)
![GitHub contributors](https://img.shields.io/github/contributors/jerimumhs/jerimumbot)
![GitHub last commit](https://img.shields.io/github/last-commit/jerimumhs/jerimumbot)


> É o bot do Telegram controlado pelo Guilherme, o gato mais bonito e simpático do mundo, com finalidade de ajudar a 
comunidade do [Jerimum Hackerspace](http://jerimumhs.org/).

## Instalação e Configuração para Desenvolvimento

Seguindo este rápido guia (desenvolvido para Linux), ao fim você será capaz de executar sua própria instância do nosso bot.

### Clonando o repositório

Para instalar o bot, o primeiro passo é clonar o repositório no seu ambiente local. Isso pode ser
feito através do seguinte comando, via terminal:

~~~~
git clone https://github.com/jerimumhs/JerimumBot.git
~~~~

Com isso pronto, basta entrar no diretório recém criado:

~~~~
cd JerimumBot/
~~~~

### Criando um ambiente virtual

Antes de prosseguir na execução do bot, você precisará criar um ambiente virtual. Existem maneiras diferentes de fazer isso, porém, nesse tutorial, mostraremos apenas uma.

Utilizando Python3, basta executar:

~~~~
python3 -m venv {{nome_do_seu_venv}}
~~~~

Onde `{{nome_do_seu_venv}}` deve ser substituído por um nome de sua escolha.

Agora, será necessário ativar este ambiente:

~~~~
source {{nome_do_seu_venv}}/bin/activate
~~~~

Para mais informações sobre o assunto, basta ler a [documentação oficial](https://docs.python.org/3/library/venv.html).

### Instalando dependências do projeto

Para essa parte do guia, você precisará ter um sistema de gerenciamento de pacotes instalado. Sugerimos que use o [pip](https://pypi.org/project/pip/).

Talvez você já tenha o `pip` instalado. Para verificar isso, basta executar:

~~~~
pip --version
~~~~

Caso não o tenha, pode simplesmente instalar via (em sistemas operacionais baseados no Ubuntu/Debian):

~~~~
sudo apt install python-pip
~~~~

Antes de prosseguir, é válido instalar estes pacotes (caso ainda não os tenha):

~~~~
sudo apt install build-essential python3-dev libssl-dev libffi-dev \
                 libxml2-dev libxslt1-dev zlib1g-dev
~~~~

Depois disso, dentro do repositório clonado, basta executar:

~~~~
pip install -r requirements.txt
~~~~

### Criando seu próprio bot no Telegram

Você precisará criar o seu próprio bot no Telegram para testar/desenvolver o JerimumBot. É um processo bastante rápido e simples.
Inicialmente, acesse a página do [BotFather](https://telegram.me/BotFather) e clique em `Send Message`.

A partir daí, o Telegram tentará abrir o aplicativo dele na sua máquina. Caso você não o tenha instalado, pode abrir o Telegram Web (ou até mesmo a versão mobile) e pesquisar por `BotFather`. Ao localizá-lo, inicie a conversa com um `/start` e siga as instruções para criar um novo bot. Ao fim, copie o token gerado, que será necessário na próxima seção.

### Configurando o .env no seu repositório local

Você já está quase lá! Agora é necessário configurar a sua versão local do `.env`. Já existe um arquivo chamado `.env.example` na raiz do diretório. Copie o conteúdo dele para um novo arquivo chamando `.env`.

Na primeira linha do arquivo você encontrará

~~~~
export BOT_TOKEN=
~~~~

O token que será colocado nessa linha é o que foi gerado quando você criou o seu bot, no passo anterior.

Por último, você precisará carregar as variáveis de ambiente do arquivo `.env` no seu terminal:

~~~~
source .env
~~~~

### Executando o JerimumBot

Depois de ter seguido todos os passos desse tutorial até aqui, você está com tudo pronto para executar o JerimumBot. Basta executar o comando `make run` e... pronto!

### Testando a sua instância

Depois disso, você pode testar as funcionalidades do JerimumBot no chat do próprio bot que você criou anteriormente. Todos os comandos do JerimumBot estarão disponíveis para você, além dos novos que você possa ter desenvolvido.

## Exemplo de uso

Em breve...

### Autores

* **Geraldo Castro** - *`Code` / `Ideas` / `Review`* - [exageraldo](https://github.com/exageraldo)
* **Rodrigo Castro** - *`Code` / `Ideas` / `Review`* - [rodrigondec](https://github.com/rodrigondec)
* **Allan Kardec** - *`Code` / `Ideas`* - [kaardeco](https://github.com/kaardeco)

## Contributing

1. Faça o _fork_ do projeto (<https://github.com/JerimumHS/JerimumBot/fork>)
2. Crie uma _branch_ para sua modificação (`git checkout -b feature/nome_da_feature`)
3. Faça o _commit_ (`git commit -am 'Add feature nome_da_feature'`)
4. _Push_ (`git push origin feature/nome_da_feature`)
5. Crie um novo _Pull Request_
6. Aguarde a _revisão_

**Esse é o seu primeiro Pull Request?** 
Você pode aprender como colaborar com esse artigo *gratuito*:
[`How to Contribute to an Open Source Project on GitHub`](https://egghead.io/series/how-to-contribute-to-an-open-source-project-on-github)

## Licença

Distribuído sob a GNU General Public License v3.0. Veja [`LICENSE`](LICENSE.md) para mais informações.
