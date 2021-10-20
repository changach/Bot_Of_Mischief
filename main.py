from logging import error
from telegram.ext import *
import config as keys
import responses as r


print("Bot Started...")


def handle_message(update, context):
    text = str(update.message.text).lower()
    response = r.bot_responses(text)

    update.message.reply_text(response)


def error(update, context):
    print(f"Update {update} caused error {context.error}")


def start_command(update, context):
    update.message.reply_text('I am at your service...Do you want to continue? (write yes if so)')


def help_command(update, context):
    update.message.reply_text('If you need help,you can ask for it on google')


def main():
    updater = Updater(keys.API, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))

    dp.add_handler(MessageHandler(Filters.text, handle_message))

    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()


main()


