from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

answer = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Відповісти користувачу",
                                             callback_data="yes"
                                         ),
                                     ]
                                 ])

stop = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Завершити бесіду",
                                             callback_data="stop"
                                         ),
                                     ]
                                 ])