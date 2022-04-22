from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters
import logging
import token

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def command_start():
    pass


def command_help():
    pass


def main() -> None:
    BotUpdater = Updater(token.token)
    dispatcher = BotUpdater.dispatcher

    dispatcher.add_handler(CommandHandler("start", command_start))
    dispatcher.add_handler(CommandHandler("help", command_help))


if __name__ == "__main__":
    main()
