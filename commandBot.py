import logging
from telegram.ext import Updater, CommandHandler
from config.auth import telegramBotToken


def start(update, context):
    """
    Defino función y texto al iniciar el bot
    """
    update.message.reply_text('Hola! Para ver una que puedo hacer, usá el comando /help')


def help(update, context):
    """
    Defino función para el comando /help
    """
    update.message.reply_text('Veamos los comandos: \n'
                              '/start - Me presento otra vez\n'
                              '/help - Ayuda de comandos'
                              )


def main():
    try:
        # Defino logeo
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

        # Defino parámetros del bot
        updater = Updater(token=telegramBotToken, use_context=True)
        dp = updater.dispatcher

        # Defino handlers
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CommandHandler("help", help))

        # Inicio bot
        updater.start_polling()
        updater.idle()

    except Exception as e:
        print(f"No se pudo iniciar el bot: {e}")


if __name__ == '__main__':
    main()

