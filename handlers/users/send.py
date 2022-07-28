from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from states.support import support
from keyboards.inline.answer import send_message

from loader import dp


@dp.message_handler(Command("send"))
async def send_message_to_users(message: types.Message):
    await message.answer('Напишіть необхідний текст для розсилки, за необхідності прікріпіть фото або файл (розсилка має містити тільки одне повідомлення)')
    support.send_message.set()

@dp.message_handler(state=support.send_message)
async def send_message(message: types.Message, state: FSMContext):
    await message.answer('Ви хочете надіслати дане повідомлення?')
    await message.copy_to(message.from_user.id, reply_markup=send_message)

@dp.callback_query_handler(text='send', state=support.send_message):
async def aplly_message(call: CallbackQuery, state: FSMContext):
    await dp.bot.copy_message()
    await call.message.answer('Повідомлення надіслано користувачам.')