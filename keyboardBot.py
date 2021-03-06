import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config.auth import telegramBotToken

# Armo Teclado
keyboard = [[InlineKeyboardButton("Opción 1", callback_data='option1'),
             InlineKeyboardButton("Opción 2", callback_data='option2')],

            [InlineKeyboardButton("Opción 3", callback_data='option3'),
             InlineKeyboardButton("Ayuda", callback_data='help')]
            ]

keyboard = InlineKeyboardMarkup(keyboard)


def button(update, context):
    """
    Defino función para responder al botón seleccionado del teclado
    """
    query = update.callback_query


    # CallbackQueries necesitan una respuesta, incluso si no se notifica al usuario
    # Algún clientes podrían tener inconvenientes. Ver https://core.telegram.org/bots/api#callbackquery
    query.answer()

    if query.data == 'option1':
        query.edit_message_text(text=f"Elegiste la opción 1", reply_markup=keyboard)
    elif query.data == 'option2':
        query.edit_message_text(text=f"Elegiste la opción 2", reply_markup=keyboard)
    elif query.data == 'option3':
        query.edit_message_text(text=f"Elegiste la opción 3", reply_markup=keyboard)
    elif query.data == 'help':
        query.edit_message_text(text=f"Soy un teclado de ejemplo.\n"
                                     f"Tocá cualquier tecla para simular una elección!", reply_markup=keyboard)


def start(update, context):
    """
    Defino función y texto al iniciar el bot
    """
    update.message.reply_text('Hola! Elegí que opción querés.',  reply_markup=keyboard)


def main():
    try:
        # Defino logeo
        logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

        # Defino parámetros del bot
        updater = Updater(token=telegramBotToken, use_context=True)
        dp = updater.dispatcher

        # Defino handlers
        dp.add_handler(CommandHandler("start", start))
        dp.add_handler(CallbackQueryHandler(button))

        # Inicio bot
        updater.start_polling()
        updater.idle()

    except Exception as e:
        print(f"No se pudo iniciar el bot: {e}")


if __name__ == '__main__':
    main()
