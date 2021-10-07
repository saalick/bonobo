import time
import requests


def telegram_bot_sendtext(bot_message):

    bot_token = '2042256304:AAHbbHMyru1f8YRyOUSQKzG0m7cPSfeR3Mg'
    bot_chatID = '@junglebookcrypto'
    send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message
    response = requests.get(send_text)
    return response.json()

msg = '''📈 What is Jungle Book Crypto? 📈
Jungle Book Crypto Token has been carefully designed to achieve a single purpose for the crypto world! Our goal is to create an all-in-one app that would benefit all the investors, traders, new projects in the space. Tokenomics has been designed in such a way that will benefit the coin and consistently take it to new heights. Our JBC Hub V1 will be released on presale, and the JBC Hub V2 will be released in Phase 1, so don't miss your chance to get in early!
Tokenomics
📈 1% Referral
🛠 1% Charity
💰 5% Auto-Liquidity
🔥 3% Unique Burn
What makes the Jungle Book Crypto so unique?  
Ur 1 Defi🦜, Hybrid Hub🐅, Exchange🐆, Staking🦒farming🎄, swap🤝, multiple currencies 💯, basecamp,
dex✅, Dapp❇️, charity😇 NFT market place✅, games🎠, and many more..📣📣💪
Revolutionizing the crypto space🌎🌎 with the JBC Hub.

Our referral program is one of a kind. For presale, anyone that refers somebody will receive 5% of their referral's initial purchase that will automatically be distributed to the referee. On our Hub V2, we will have a little bit more incentive as anyone that refers somebody will receive 1% of their purchase continuously as long as they purchase Jbc on our platform. The referral program is just one way the JBC team recognizes the JBC community, so stay tuned as the JBC team has many more incentives for you!!!!
Presale will start soon💯🔥🔥🚀🚀
🌐 Telegram - @junglebookcrypto
🌐 Website - junglebookcrypto.com
'''
while(True):
 telegram_bot_sendtext(msg)
 time.sleep(7200)


