from aiogram import types
from utils.misc.environments_for_db import start_comand

async def set_default_commands(dp):
    await dp.bot.set_my_commands(
        [
            types.BotCommand("start", start_comand),
        ]
    )
