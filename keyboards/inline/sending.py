from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

send_messages = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text="Надіслати",
                                                callback_data="send"
                                            ), InlineKeyboardButton(
                                                text="Скасувати",
                                                callback_data="no_send"
                                            ),
                                        ],
                                        [
                                            InlineKeyboardButton(
                                                text="Редагувати",
                                                callback_data="edit"
                                            ),
                                        ]
                                    ])

cancel = InlineKeyboardMarkup(row_width=2, inline_keyboard=[
                                        [
                                            InlineKeyboardButton(
                                                text="Скасувати",
                                                callback_data="no_send"
                                            ),
                                        ],

                                    ])