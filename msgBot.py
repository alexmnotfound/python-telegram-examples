import telegram
from config.auth import telegramBotToken, telegramID


def sendMsg(ID=telegramID, msg=''):
    """
    Envía mensaje a ID determinado.
    """

    bot = telegram.Bot(token=telegramBotToken)

    bot.sendMessage(chat_id=ID,
                    text=f'{msg}')

sendMsg(msg='Hello there')