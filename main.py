import time
import requests


def telegram_bot_sendtext(bot_message):

    bot_token = '#'
    bot_chatID = '#'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

msg = '''  💎For LIVE JBC Presale visit 🌐 http://bit.ly/3cDVHGm
Min buy 0.1 BNB max buy 5 BNB.

Check pinned video for "How to buy JBC on Pinksale" for instructions.

Ask our Jungle Guides for more info.⚜️ '''
while(True):
 telegram_bot_sendtext(msg)
 time.sleep(3600)
 time.sleep(3600)



