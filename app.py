from aiogram import executor

from loader import dp
import middlewares, filters, handlers
from utils.db_api.environments_for_db import get_db, db
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    # Завантажуємо базу даних
    await get_db()

    # Встановлюємо дефолтні команди
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

