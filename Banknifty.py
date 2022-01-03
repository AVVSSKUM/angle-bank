import json
import requests
import time
from smartapi.smartConnect import SmartConnect
api_key = 'rDqE7Caq'
UserId = 'A114028'
Password = 'SYAM2831#123'
obj = SmartConnect(api_key=api_key)
data = obj.generateSession(UserId, Password)
refreshToken = data['data']['refreshToken']
flag = 0
bot_token = '2128421945:AAHz-s9UwmnCoXP4zbcQjTUm5KSS0EtHzl8'
bot_chatID = '1142557708'
symbol = 'BANKNIFTY'
symbol1 = 'NIFTY'
def telegram_bot_sendtext(bot_message):
    send_text= 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode = MarkdownV2&text=' +bot_message
    response = requests.get(send_text)
    return response.json()
while(True):
     curr_price = obj.ltpData('NSE', symbol, 26009)['data']['ltp']
     curr_price1 = obj.ltpData('NSE', symbol1, 26000)['data']['ltp']
     telegram_bot_sendtext("Banknifty:")
     telegram_bot_sendtext(str(curr_price))
     telegram_bot_sendtext("Nifty:")
     telegram_bot_sendtext(str(curr_price1))
     time.sleep(3600)
