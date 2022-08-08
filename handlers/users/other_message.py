from loader import dp
from aiogram import types

from utils.cheks import is_operator


@dp.message_handler(content_types=types.ContentType.ANY)
async def any_message(message: types.Message):
    if not is_operator(message.from_user.id):
        await message.answer("Для підключення спеціаліста оберіть команду /start")