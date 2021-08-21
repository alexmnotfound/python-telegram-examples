import telegram
from config.auth import telegramBotToken, telegramID


def sendMsg(ID=telegramID, msg=''):
    """
    Envía mensaje a ID determinado.
    """
    try:
        bot = telegram.Bot(token=telegramBotToken)

        bot.sendMessage(chat_id=ID,
                        text=f'{msg}')
    except Exception as e:
        print(f"No se pudo iniciar bot: {e}")


def main():
    try:
        sendMsg(msg='Hello there')

    except Exception as e:
        print(f"No se pudo enviar mensaje: {e}")


if __name__ == '__main__':
    main()
