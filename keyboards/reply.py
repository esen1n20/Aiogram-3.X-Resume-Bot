from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


main_kb = ReplyKeyboardMarkup(
    keyboard = [
        [
            KeyboardButton(text = "СОЗДАТЬ ВЕСТОЧКУ"),
        ],    
        [    
            KeyboardButton(text = "О НАС НАФИГ")
        ]
    ],
    resize_keyboard=True
)

