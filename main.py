import time
import requests


def telegram_bot_sendtext(bot_message):

    bot_token = '2042256304:AAEkOR4bRxiWb35D4PAQut9b_ifXVQDEBRo'
    bot_chatID = '@junglebookcrypto'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

msg = '''💎For presale visit us at🌐 www.junglebookcrypto.com  click on the buy now button where it will take you to create an account and purchase the token. 💰The only method of payment the jungle accepts is BNB and Buy Through PinkSale with the Pinksale link https://www.pinksale.finance/#/launchpad/0xE9ACbA178F2199Bb851090c6EcdE4A72F3793d32?chain=BSC 
Min buy 0.1 BNB max buy 5 BNB. Also please see the referral info.🤑 The Jungle has a great referral package for all its members!!!!!!!!! Ask our Jungle Guides for more info.⚜️ '''
while(True):
 telegram_bot_sendtext(msg)
 time.sleep(3600)
 time.sleep(3600)



