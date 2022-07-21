from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.dispatcher.filters.state import StatesGroup, State
from aiogram.types import CallbackQuery

from keyboards.inline.answer import answer, stop

from loader import dp

class support(StatesGroup):
    suport_call = State()


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if message.from_user.id != 178875921:
        global current_user_id
        current_user_id = int(message.from_user.id)
        main_text = f"Доброго дня, {message.from_user.full_name}!\nНаш оператор служби підтримки вже підключається до розмови."
        await message.answer(main_text)
        user_name = message.from_user.full_name

        await dp.bot.send_message(178875921, f'Користувач, {user_name}, потребує підтримки', reply_markup=answer)
        await support.suport_call.set()

@dp.callback_query_handler(text='yes')
async def confirm_support(call: CallbackQuery):
    await call.answer(cache_time=10)
    await call.message.edit_reply_markup(None)
    await call.message.answer('Для завершення розмови натисніть кнопку', reply_markup=stop)
    await dp.bot.send_message(current_user_id, 'Адміністратор підключився до розмови.')
    await support.suport_call.set()

@dp.callback_query_handler(text='stop', state=support.suport_call)
async def cansel_support(call: CallbackQuery, state: FSMContext):
    await call.answer(cache_time=10)
    await call.message.edit_reply_markup(None)
    await dp.bot.send_message(current_user_id, 'Адміністратор завершив бесіду')
    await call.message.answer('Ви завершили бесіду')
    user_state = dp.current_state(chat=current_user_id, user=current_user_id)
    await state.finish()
    await user_state.finish()

@dp.message_handler(state=support.suport_call, content_types=types.ContentType.ANY)
async def support_call(message: types.message):
    admin_id = '178875921'

    if message.from_user.id != int(admin_id):
        await message.copy_to(admin_id)
    elif message.from_user.id == int(admin_id):
        await message.copy_to(current_user_id)