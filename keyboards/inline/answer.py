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

stop = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Завершити бесіду",
                                             callback_data="stop",
                                         ),
                                     ]
                                 ])

send_message = InlineKeyboardMarkup(row_width=2, one_time_keyboard=True,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(
                                             text="Відправити",
                                             callback_data="send",
                                         ),

                                     ],
                                     [
                                         InlineKeyboardButton(
                                             text="Відмінити відправку",
                                             callback_data="no_send",
                                         ),
                                     ],
                                     [
                                         InlineKeyboardButton(
                                             text="Змінити повідомлення",
                                             callback_data="edit",
                                         ),
                                     ]
                                 ])