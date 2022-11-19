import logging
import sys
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

from telegram import KeyboardButton, ReplyKeyboardMarkup

from task import Task
import data

import random
from datetime import datetime
random.seed(datetime.now().microsecond)

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)


def reply_keyboard_markup():
    keyboard = [[KeyboardButton("/next")]]
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


async def next(update: Update, context: ContextTypes.DEFAULT_TYPE):
    task = Task(*data.get4())
    await context.bot.send_poll(
        type="quiz",
        chat_id=update.effective_chat.id,
        question=task.question(),
        options=task.options(),
        correct_option_id=task.correct(),
        reply_markup=reply_keyboard_markup()
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


if __name__ == '__main__':
    secret = open('secret').read()
    application = ApplicationBuilder().token(secret).build()

    start_handler = CommandHandler('start', start)
    application.add_handler(start_handler)

    next_handler = CommandHandler('next', next)
    application.add_handler(next_handler)

    shutdown_handler = CommandHandler('shutdown', shutdown)
    application.add_handler(shutdown_handler)

    application.run_polling()
