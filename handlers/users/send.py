import time

from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery
from states.support import support
from keyboards.inline.sending import send_messages, cancel
from utils.db_api.dbconfig import get_all_users


@dp.message_handler(Command("send"))
async def send_message_to_users(message: types.Message):
    await message.answer('Напишіть необхідний текст для розсилки, за необхідності прікріпіть фото або файл (розсилка має містити тільки одне повідомлення)', reply_markup=cancel)
    await support.send_message.set()

@dp.message_handler(state=support.send_message, content_types=types.ContentType.ANY)
async def send_message(message: types.Message):
    await message.copy_to(message.from_user.id, reply_markup=send_messages)
    await message.delete()

@dp.callback_query_handler(state=support.send_message, text='send')
async def aplly_message(call: CallbackQuery, state: FSMContext):
    await call.message.delete_reply_markup()
    users = await get_all_users()
    counter = 0
    for user in users:
        if counter == 30:
            time.sleep(1)
            counter = 0
        try:
            await call.message.copy_to(chat_id=user)
            counter += 1
        except:
            pass

    await dp.bot.delete_message(chat_id=call.message.chat.id, message_id=(call.message.message_id - 2))
    await call.message.answer('Повідомлення надіслано користувачам.')
    await state.finish()



@dp.callback_query_handler(state=support.send_message, text='no_send')
async def cancel_message(call: CallbackQuery, state: FSMContext):
    try:
        await dp.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
        await dp.bot.delete_message(chat_id=call.message.chat.id, message_id=(call.message.message_id - 2))
    except:
        pass
    await call.message.answer('Надсилання повідомлень скасовано.')
    await state.finish()

@dp.callback_query_handler(state=support.send_message, text='edit')
async def edit_message(call: CallbackQuery):
    await dp.bot.delete_message(chat_id=call.message.chat.id, message_id=(call.message.message_id - 2))
    await dp.bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
    await call.message.answer(
        'Напишіть необхідний текст для розсилки, за необхідності прікріпіть фото або файл (розсилка має містити тільки одне повідомлення)', reply_markup=cancel)