from aiogram import Router, types
from aiogram.filters import Command
from bot.keyboards.main import get_main_keyboard

router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer(
        f" <b>Привет, {message.from_user.full_name}!</b>\n\n"
        " Я <b>Telegram MultiBot Pro</b> — твой многофункциональный помощник!\n\n"
        " <b>Что я умею:</b>\n"
        " <b>Погода</b> — актуальная погода в любом городе\n"
        " <b>Валюты</b> — курсы и конвертер\n"
        " <b>ChatGPT</b> — диалоговый ИИ\n"
        " <b>QR-коды</b> — генератор\n"
        " <b>Статистика</b> — твои достижения\n"
        " <b>Мини-игры</b> — развлечения\n\n"
        " Используй меню для навигации!",
        reply_markup=get_main_keyboard()
    )

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer(
        " <b>Помощь по командам:</b>\n\n"
        "/start - Главное меню\n"
        "/help - Эта справка\n"
        "/weather [город] - Погода\n"
        "/currency - Курсы валют\n"
        "/gpt [вопрос] - ChatGPT\n"
        "/qrcode [текст] - QR-код\n"
        "/stats - Статистика\n"
        "/game - Мини-игры\n\n"
        "Или просто используй кнопки меню! "
    )
