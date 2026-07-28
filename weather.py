from aiogram import Router, types, F
from aiogram.filters import Command
from bot.keyboards.weather import get_cities_keyboard, get_back_keyboard
from bot.services.weather import WeatherService
from bot.utils.formatters import format_weather

router = Router()
weather_service = WeatherService()

@router.message(F.text == "Погода")
@router.message(Command("weather"))
async def weather_menu(message: types.Message):
    await message.answer(
        " <b>Погода</b>\n\n"
        "Выбери город из списка или напиши название:",
        reply_markup=get_cities_keyboard()
    )

@router.callback_query(F.data.startswith("weather_city:"))
async def weather_city_callback(callback: types.CallbackQuery):
    city = callback.data.split(":")[1]
    await callback.answer(" Получаю данные о погоде...")
    
    weather_data = await weather_service.get_weather(city)
    
    if weather_data:
        await callback.message.edit_text(
            format_weather(weather_data),
            reply_markup=get_back_keyboard()
        )
    else:
        await callback.answer(" Город не найден", show_alert=True)

@router.message(F.text.regexp(r"^[А-Яа-яA-Za-z\s\-]+$"))
async def weather_custom_city(message: types.Message):
    weather_data = await weather_service.get_weather(message.text)
    
    if weather_data:
        await message.answer(
            format_weather(weather_data),
            reply_markup=get_back_keyboard()
        )
    else:
        await message.answer("Не удалось найти город. Проверь название.")
