import logging
import configparser
from exchange_bot import ExchangeBot 

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

def main() -> None:
    config = configparser.ConfigParser()
    config.read('/usr/local/etc/telegram/bot/tokens.conf')        
    bot = ExchangeBot(config['bot']['token'])
    bot.run()

if __name__ == "__main__":
    main()