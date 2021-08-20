import telegram

telegramBotToken = '1262404873:AAEG6hMSQCD19kFBL1wFVogilR6A21VQaW4'
telegramGroupID = '-418631633'

def sendMsg(ID=telegramGroupID, msg=''):
    """
    Send Telegram Message to selected ID.
    """


    bot = telegram.Bot(token=telegramBotToken)

    bot.sendMessage(chat_id=ID,
                    text=f'{msg}')

sendMsg(msg='test')