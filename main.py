import logging
from santantoni.config import config
from santantoni.core import SantAntoniBot


def setup_logging():
    if config.DEBUG:
        logging.basicConfig(
            level=logging.DEBUG,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
        )


def main():
    bot = SantAntoniBot(config.TELEGRAM_TOKEN)
    try:
        bot.start()
    except KeyboardInterrupt:
        exit(1)


if __name__ == '__main__':
    setup_logging()
    main()