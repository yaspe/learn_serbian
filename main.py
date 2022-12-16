from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, PollHandler

from telegram import KeyboardButton, ReplyKeyboardMarkup

from task import Task
from word import Word
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
        text="I'm a Serbian bot and I'l help you to learn Serbian. I know %i phrases. To get a question print or tap /next" % storage.count_words(),
        reply_markup=reply_keyboard_markup()
    )


async def topics(update: Update, context: ContextTypes.DEFAULT_TYPE):
    markup = ReplyKeyboardMarkup(
        [[KeyboardButton("/next " + topic)] for topic in storage.list_topics_names()],
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
        name = text.split(' ')[-1]
        topic = (storage.get_topic_id(name), name)
    else:
        topic = storage.get_random_topic()

    raw_words = storage.get_some_words_by_topic(topic[0])
    words = [Word(raw[2], raw[3]) for raw in raw_words]
    task = Task(*words)

    message = await update.effective_message.reply_poll(
        type="quiz",
        question=task.question(),
        options=task.options(),
        correct_option_id=task.correct(),
        reply_markup=reply_keyboard_markup(topic[1])
    )
    payload = {
        message.poll.id: {"chat_id": update.effective_chat.id, "message_id": message.message_id}
    }
    context.bot_data.update(payload)


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


async def receive_quiz_answer(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.poll.total_voter_count != 1:
        return
    chat_id = context.bot_data[update.poll.id]['chat_id']
    is_correct = update.poll.options[update.poll.correct_option_id].voter_count == 1
    storage.add_answer(chat_id, is_correct)

    print(storage.get_user_stat(chat_id))


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

    application.add_handler(PollHandler(receive_quiz_answer))

    application.run_polling()
