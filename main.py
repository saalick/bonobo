import time
import requests


def telegram_bot_sendtext(bot_message):

    bot_token = '2042256304:AAHbbHMyru1f8YRyOUSQKzG0m7cPSfeR3Mg'
    bot_chatID = '@junglebookcrypto'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

msg = '''Jungle Book Crypto
Ur 1 Defi🦜, Hybrid Hub🐅, Exchange🐆, Staking
🦒 farming🎄, swap🤝, multiple currency💯,
dex✅,Dapp❇️,charity😇 nft market place✅,
games🎠,  and many more..📣📣💪
Revolutionising the crypto space🌎🌎 with the JBC Hub.
Pre sale will start soon💯🔥🔥'''
while(True):
 telegram_bot_sendtext(msg)
 time.sleep(7200)


