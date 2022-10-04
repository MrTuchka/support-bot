import logging

from data.config import BOT_TOKEN, WEBHOOK_URL
from loader import dp, bot
from aiogram import Bot, Dispatcher
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.executor import start_webhook


import middlewares, filters, handlers
from utils.db_api.environments_for_db import get_db, db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


# webhook settings
WEBHOOK_HOST = WEBHOOK_URL
WEBHOOK_PATH = f'/bot/{BOT_TOKEN}'
WEBHOOK_MAIN_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"

# webserver settings
WEBAPP_HOST = '127.0.0.1'  # or ip
WEBAPP_PORT = "5000"

logging.basicConfig(level=logging.INFO)

dp.middleware.setup(LoggingMiddleware())

async def on_startup(dispatcher):
    await bot.set_webhook(WEBHOOK_MAIN_URL)

    # Завантажуємо базу даних
    await get_db()

    # Встановлюємо дефолтні команди
    await set_default_commands(dispatcher)


async def on_shutdown(dispatcher):
    logging.warning('Shutting down..')

    # insert code here to run it before shutdown

    # Remove webhook (not acceptable in some cases)
    await bot.delete_webhook()

    # Close DB connection (if used)
    await dispatcher.storage.close()
    await dispatcher.storage.wait_closed()

    logging.warning('Bye!')


if __name__ == '__main__' and WEBHOOK_URL != "":
    start_webhook(
        dispatcher=dp,
        webhook_path=WEBHOOK_PATH,
        on_startup=on_startup,
        on_shutdown=on_shutdown,
        skip_updates=True,
        host=WEBAPP_HOST,
        port=WEBAPP_PORT,
    )

