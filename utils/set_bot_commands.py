from aiogram import types
from aiogram.types import BotCommandScopeChat

from data.config import ADMINS
from utils.db_api.environments_for_db import db


async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", str(db.get("start_command"))),
        ]
    )

#Команди, які бачать тільки адмінітсратори
    for admin in ADMINS:
        await dp.bot.set_my_commands(
        [
            types.BotCommand("start", str(db.get("start_command"))),
            types.BotCommand("send", str(db.get("send_command"))),
        ], BotCommandScopeChat(chat_id=admin)
    )