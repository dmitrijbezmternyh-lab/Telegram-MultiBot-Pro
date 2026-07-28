from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder

def get_main_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    
    builder.row(
        KeyboardButton(text=" Погода"),
        KeyboardButton(text=" Валюты"),
        width=2
    )
    builder.row(
        KeyboardButton(text=" Assistent"),
        KeyboardButton(text=" QR-код"),
        width=2
    )
    builder.row(
        KeyboardButton(text=" Игры"),
        KeyboardButton(text=" Статистика"),
        width=2
    )
    builder.row(
        KeyboardButton(text=" Помощь")
    )
    
    return builder.as_markup(resize_keyboard=True)

def get_back_to_main_keyboard() -> ReplyKeyboardMarkup:
    builder = ReplyKeyboardBuilder()
    builder.add(KeyboardButton(text=" Главное меню"))
    return builder.as_markup(resize_keyboard=True)
