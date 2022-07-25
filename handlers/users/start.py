import re
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import CallbackQuery
from utils.cheks import is_operator, curent_user
from data.config import ADMINS
from states.support import support
from keyboards.inline.answer import answer, stop
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    if not is_operator(message.from_user.id):

        main_text = f"Доброго дня, {message.from_user.full_name}!\n" \
                    f"Наш оператор служби підтримки вже підключається до розмови."
        await message.answer(main_text)
        # Надсилання повідомлення усім операторам зі списку
        for admin in ADMINS:
            await dp.bot.send_message(admin,
                                      f'Користувач, {message.from_user.full_name}, потребує підтримки.\nid: <i>{message.from_user.id}</i>',
                                      reply_markup=answer, parse_mode="html")


@dp.callback_query_handler(text='yes')
async def confirm_support(call: CallbackQuery, state: FSMContext):
    current_user = re.findall('\d+', f"{call.message.text}")[0]
    if await curent_user(current_user):
        await support.in_call.set()
        current_admin = call.message.chat.id
        await state.update_data({'user': current_user,
                                 'admin': current_admin})

        data_admin = await state.get_data()
        user = data_admin.get('user')

        user_state = dp.current_state(chat=user, user=user)
        await user_state.set_state(state=support.in_call)
        await user_state.update_data(data_user_id=user)

        data_user = await user_state.update_data({'user': current_user,
                                                  'admin': current_admin})

        await call.answer(cache_time=10)
        await call.message.edit_reply_markup(stop)
        await call.message.answer("Ви на зв'язку з користувачем.")
        await dp.bot.send_message(user, 'Адміністратор підключився до розмови.')
    else:
        await call.answer(cache_time=10)
        await call.message.answer("Користувач вже підключений до іншого оператора.")


@dp.callback_query_handler(text='stop', state=support.in_call)
async def cansel_support_0(call: CallbackQuery, state: FSMContext):
    try:
        admin_data = await state.get_data()
        user = admin_data.get('user')

        user_state = dp.current_state(chat=user, user=user)

        user_data = await user_state.get_data()
        admin = user_data.get('admin')

        await call.answer(cache_time=10)
        await call.message.edit_reply_markup(None)
        await dp.bot.send_message(user, 'Адміністратор завершив бесіду')
        await call.message.answer('Ви завершили бесіду')
        user_state = dp.current_state(chat=user, user=user)
        await state.finish()
        await user_state.finish()
    except:
        await call.message.answer('Ви завершили бесіду')


@dp.callback_query_handler(text='stop')
async def cansel_support_without_state(call: CallbackQuery):
    await call.message.answer('Ви завершили бесіду')
    await call.message.edit_reply_markup(None)


@dp.message_handler(state=support.in_call, content_types=types.ContentType.ANY)
async def support_call_0(message: types.message, state: FSMContext):
    try:
        admin_data = await state.get_data()
        user = admin_data.get('user')

        user_state = dp.current_state(chat=user, user=user)
        current_state = await user_state.get_state()

        user_data = await user_state.get_data()
        admin = user_data.get('admin')

        if current_state == 'support:in_call':
            if message.from_user.id != admin:
                await message.copy_to(admin)
            elif message.from_user.id == admin:
                await message.copy_to(user)
    except:
        admin_data = await state.get_data()
        user = admin_data.get('user')

        user_state = dp.current_state(chat=user, user=user)

        user_data = await user_state.get_data()
        admin = user_data.get('admin')
        await dp.bot.send_message(admin, 'Користувач заблокував бота.')
        await state.finish()