import logging

from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


def escape(self):
    escape_chars = {'[': '\\[', '`': '\\`', '_': '\\_', '*': '\\*'}
    return ''.join(escape_chars.get(c, c) for c in self)


def reply_to_message(update: Update, context: CallbackContext) -> None:
    if (update.message.text.replace("/", "").isascii() and not update.message.text.startswith('/$')) \
            or update.message.text.replace("/$", "") == '':
        return
    if update.message.reply_to_message is None:
        reply_to = '自己'
        reply_to_id = update.message.from_user.id
    else:
        reply_to = update.message.reply_to_message.from_user.full_name
        reply_to_id = update.message.reply_to_message.from_user.id
    user = update.effective_user
    logger.info(f'User {user.id} replied to a message at Chat {update.message.chat_id}')
    update.message.reply_markdown(
        fr'[{escape(user.full_name)}](tg://user?id={user.id})  {escape(update.message.text.replace("/", "").replace("$", ""))}了  [{reply_to}](tg://user?id={reply_to_id}) '
    )


def main() -> None:
    bot_updater = Updater('1812845876:AAGdbOKUVOOZ7LekOnvU6D8dIwzKZmM-tro')
    dispatcher = bot_updater.dispatcher

    dispatcher.add_handler(MessageHandler(Filters.text, reply_to_message))

    bot_updater.start_polling()
    bot_updater.idle()


if __name__ == "__main__":
    main()
