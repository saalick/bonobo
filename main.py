import time
import requests


def telegram_bot_sendtext(bot_message):

    bot_token = '2042256304:AAFYjhnzPO3VgZteS7v1DbocKfKJy9V7UeY'
    bot_chatID = '@junglebookcrypto'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

msg = '''  πFor LIVE JBC Presale visit π http://bit.ly/3cDVHGm
Min buy 0.1 BNB max buy 5 BNB.

Check pinned video for "How to buy JBC on Pinksale" for instructions.

Ask our Jungle Guides for more info.βοΈ '''
while(True):
 telegram_bot_sendtext(msg)
 time.sleep(3600)
 time.sleep(3600)



