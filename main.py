import logging
import os

import telegram
import telegram.ext
from telegram.ext.dispatcher import run_async

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG
)

logger = logging.getLogger(__name__)


def escape(self):
    escape_chars = {'[': '\\[', '`': '\\`', '_': '\\_', '*': '\\*'}
    return ''.join(escape_chars.get(c, c) for c in self)

@run_async
def reply_to_message(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    if (update.message.text.replace("/", "").isascii() and not update.message.text.startswith('/$')) \
            or not update.message.text.startswith('/') or update.message.text.replace("/$", "") == '':
        return
    if update.message.reply_to_message is None:
        reply_to = '自己'
        reply_to_id = update.message.from_user.id
    else:
        reply_to = update.message.reply_to_message.from_user.full_name
        reply_to_id = update.message.reply_to_message.from_user.id

    user = update.effective_user
    logger.info(f'User {user.id} replied to a message at Chat {update.message.chat_id}')

    keywords = update.message.text.replace("/", "").replace("$", "").split(' ', maxsplit=1)

    if len(keywords) == 1:
        update.message.reply_markdown(
            fr'[{escape(user.full_name)}](tg://user?id={user.id}) {escape(keywords[0])}了 [{reply_to}](tg://user?id={reply_to_id})！'
        )
    else:
        update.message.reply_markdown(
            fr'[{escape(user.full_name)}](tg://user?id={user.id}) {escape(keywords[0])} [{reply_to}](tg://user?id={reply_to_id}) {escape(keywords[1])}！'
        )


def main() -> None:
    bot_updater = telegram.ext.Updater(os.environ.get("BOT_TOKEN"))
    dispatcher = bot_updater.dispatcher

    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, reply_to_message))

    bot_updater.start_polling()
    bot_updater.idle()


if __name__ == "__main__":
    main()
