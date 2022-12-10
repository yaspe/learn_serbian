from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from telegram import KeyboardButton, ReplyKeyboardMarkup

from task import Task
import data
from storage import Storage

import random
from datetime import datetime
random.seed(datetime.now().microsecond)

storage = Storage()


def reply_keyboard_markup(topic=''):
    keyboard = [[KeyboardButton("/next")], [KeyboardButton("/next " + topic), KeyboardButton("/topics")]]
    return ReplyKeyboardMarkup(
        keyboard,
        resize_keyboard=True,
        one_time_keyboard=True,
    )


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="I'm a Serbian bot and I'l help you to learn Serbian. I know %i phrases. To get a question print or tap /next" % data.count(),
        reply_markup=reply_keyboard_markup()
    )


async def topics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    markup = ReplyKeyboardMarkup(
        [[KeyboardButton("/next " + topic)] for topic in data.get_topics()],
        resize_keyboard=True,
        one_time_keyboard=True,
    )
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Select a topic",
        reply_markup=markup
    )


async def next(update: Update, context: ContextTypes.DEFAULT_TYPE):
    storage.add_user(update.effective_chat.username, update.effective_chat.id)

    text = update.message.text
    if text != "/next":
        topic = text.split(' ')[-1]
    else:
        topic = data.get_random_topic()
    task = Task(*data.get_by_topic(topic))

    await context.bot.send_poll(
        type="quiz",
        chat_id=update.effective_chat.id,
        question=task.question(),
        options=task.options(),
        correct_option_id=task.correct(),
        reply_markup=reply_keyboard_markup(topic=topic)
    )


async def shutdown(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != 37129726:
        return
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="ok"
    )
    import os
    import signal
    os.kill(os.getpid(), signal.SIGINT)


async def stat(update: Update, context: ContextTypes.DEFAULT_TYPE):
    if update.effective_chat.id != 37129726:
        return
    users = storage.list_users()

    try:
        stats = 'Users: %i\n\n%s' % (len(users), '\n'.join(users))
    except Exception as e:
        stats = str(e)

    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=stats
    )


if __name__ == '__main__':
    secret = open('secret').read()
    application = ApplicationBuilder().token(secret).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    next_handler = CommandHandler('next', next)
    application.add_handler(next_handler)

    topics_handler = CommandHandler('topics', topics)
    application.add_handler(topics_handler)

    shutdown_handler = CommandHandler('shutdown', shutdown)
    application.add_handler(shutdown_handler)

    stat_handler = CommandHandler('stat', stat)
    application.add_handler(stat_handler)

    application.run_polling()
