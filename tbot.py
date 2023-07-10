import logging
import configparser
# from exchange_bot import ExchangeBot 
from chat_bot import TelegramChatBot 
from chat_gpt import ChatGPT
from user_db import UserDB
import traceback

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    token = configparser.ConfigParser()
    token.read('/usr/local/etc/mytbot/tokens.conf')

    config = configparser.ConfigParser()
    config.read('/usr/local/etc/mytbot/bot.conf')       

    global telegram_db
    telegram_db = UserDB(config['db']['path'])
    
    global chatgpt
    chatgpt = ChatGPT(token['chatgpt']['token'])

    bot = TelegramChatBot(token['bot']['token'], api_token_handler)
    bot.set_message_handler(request_handler)
    bot.run()

def api_token_handler(userid, username, api_key):
    try:
        telegram_db.insert(userid, username, api_key)
        return "You are registerd now with your api_key"
    except:
        return "An error occured in api_key registration"

def request_handler(userid, request):
    try:
        api_key = telegram_db.api_key(str(userid))
        print(userid)
        print(request)
        print(api_key)
        if api_key:
            return chatgpt.chat(api_key, request)
        else:
            print("1")
            return "You have to first register yourself with openai API_KEY!!!"
    except Exception:
        traceback.print_exc()
        return "You have to first register yourself with openai API_KEY!!!"    

if __name__ == "__main__":
    main()