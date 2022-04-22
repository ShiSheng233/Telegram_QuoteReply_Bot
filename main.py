import telegram, telegram.ext, logging

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)

"""
def command_start(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    user = update.effective_user
    logger.info(f'User {user.id} tapped \'/start\'')
    update.message.reply_markdown_v2(
        fr'Hello {user.mention_markdown_v2()}\!'
    )


def command_help(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    user = update.effective_user
    logger.info(f'User {user.id} tapped \'/help\'')
    update.message.reply_markdown_v2(
        'qwq'
    )
"""


def reply_to_message(update: telegram.Update, context: telegram.ext.CallbackContext) -> None:
    user = update.effective_user
    logger.info(f'User {user.id} replied to a message at Chat {update.message.chat_id}')
    update.message.reply_markdown_v2(
        fr'`{user.full_name}` {update.message.text.replace("/", "")}了 `{update.message.reply_to_message.from_user.full_name}`'
    )


def main() -> None:
    BotUpdater = telegram.ext.Updater("""Your BOT Token Here""")
    dispatcher = BotUpdater.dispatcher

    # dispatcher.add_handler(telegram.ext.CommandHandler("start", command_start))
    # dispatcher.add_handler(telegram.ext.CommandHandler("help", command_help))
    dispatcher.add_handler(telegram.ext.MessageHandler(telegram.ext.Filters.text, reply_to_message))

    BotUpdater.start_polling()
    BotUpdater.idle()


if __name__ == "__main__":
    main()
