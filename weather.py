from aiogram.types import InlineKeyboardMarkup,InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder

inline_menu = InlineKeyboardMarkup(
    inline_keyboard= [

    {InlineKeyboardButton(text="Navoiy",callback_data="navoiy"),
    InlineKeyboardButton(text="Fargona",callback_data="fargona"),},

    {InlineKeyboardButton(text="Vobkent",callback_data="vobkent"),
    InlineKeyboardButton(text="Andijon",callback_data="andijon")},

    {InlineKeyboardButton(text="Jizzax",callback_data="jizzax"),
    InlineKeyboardButton(text="Qarshi",callback_data="qarshi")},
    ]
)

 