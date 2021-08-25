import logging
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from config.auth import telegramBotToken

# Armo Teclado Principal

welcomeMsg = 'Hola! Elegí que opción querés.'

keyboard1 = [[InlineKeyboardButton("Opción 1", callback_data='option1'),
             InlineKeyboardButton("Opción 2", callback_data='option2')],

            [InlineKeyboardButton("Más opciones >>", callback_data='moreOptions'),
             InlineKeyboardButton("Ayuda", callback_data='help')]
            ]

keyboard1 = InlineKeyboardMarkup(keyboard1)

# Armo Teclado Secundario
keyboard2 = [[InlineKeyboardButton("Opción 3", callback_data='option3'),
             InlineKeyboardButton("Opción 4", callback_data='option4')],

            [InlineKeyboardButton("<< Atrás", callback_data='backToKb1')]
            ]

keyboard2 = InlineKeyboardMarkup(keyboard2)


def button(update, context):
    """
    Defino función para responder al botón seleccionado del teclado
    """
    query = update.callback_query


    # CallbackQueries necesitan una respuesta, incluso si no se notifica al usuario
    # Algunos clientes podrían tener inconvenientes. Ver https://core.telegram.org/bots/api#callbackquery
    query.answer()

    if query.data == 'option1':
        query.edit_message_text(text=f"Elegiste la opción 1", reply_markup=keyboard1)
    elif query.data == 'option2':
        query.edit_message_text(text=f"Elegiste la opción 2", reply_markup=keyboard1)
    elif query.data == 'moreOptions':
        query.edit_message_text(text=f"Menú secundario", reply_markup=keyboard2)
    elif query.data == 'help':
        query.edit_message_text(text=f"Soy un teclado de ejemplo.\n"
                                     f"Tocá cualquier tecla para simular una elección!", reply_markup=keyboard1)
    elif query.data == 'option3':
        query.edit_message_text(text=f"Elegiste la opción 3", reply_markup=keyboard2)
    elif query.data == 'option4':
        query.edit_message_text(text=f"Elegiste la opción 4", reply_markup=keyboard2)
    elif query.data == 'backToKb1':
        query.edit_message_text(text=welcomeMsg, reply_markup=keyboard1)


def start(update, context):
    """
    Defino función y texto al iniciar el bot
    """
    update.message.reply_text(welcomeMsg,  reply_markup=keyboard1)


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
