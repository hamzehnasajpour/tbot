import logging
import configparser
# from exchange_bot import ExchangeBot 
from chat_bot import TelegramChatBot 
from chat_gpt import ChatGPT

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    config = configparser.ConfigParser()
    config.read('/usr/local/etc/mytbot/tokens.conf')        

    chatgpt = ChatGPT(config['chatgpt']['token'])

    bot = TelegramChatBot(config['bot']['token'])
    bot.set_message_handler(chatgpt.chat)
    bot.run()


if __name__ == "__main__":
    main()