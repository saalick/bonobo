import time
import requests


def telegram_bot_sendtext(bot_message):

    bot_token = '2042256304:AAEkOR4bRxiWb35D4PAQut9b_ifXVQDEBRo'
    bot_chatID = '@junglebookcrypto'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

msg = '''My name is Bonobo🐻, and I am excited to have you enter the Jungle. 🌲🦧 We have just migrated to Pinksale. Please visit their site for the presale!! 
Thank you all and welcome new members to the Jungle!!!!🌴👑🚀🚀

http://bit.ly/3cDVHGm'''
while(True):
 telegram_bot_sendtext(msg)
 time.sleep(3600)
 time.sleep(3600)



