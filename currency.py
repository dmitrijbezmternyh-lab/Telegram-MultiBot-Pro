from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from bot.keyboards.currency import get_currency_keyboard, get_converter_keyboard
from bot.services.currency import CurrencyService
from bot.states.currency_states import CurrencyConverter
from bot.utils.formatters import format_rates, format_conversion

router = Router()
currency_service = CurrencyService()

@router.message(F.text == "Валюты")
@router.message(Command("currency"))
async def currency_menu(message: types.Message):
    rates = await currency_service.get_rates()
    
    if rates:
        await message.answer(
            format_rates(rates),
            reply_markup=get_currency_keyboard()
        )
    else:
        await message.answer("Не удалось загрузить курсы валют")

@router.callback_query(F.data == "currency_convert")
async def start_converter(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer()
    await callback.message.answer(
        "<b>Конвертер валют</b>\n\n"
        "Введи сумму для конвертации (например: 100):",
        reply_markup=get_converter_keyboard()
    )
    await state.set_state(CurrencyConverter.amount)

@router.message(CurrencyConverter.amount)
async def process_amount(message: types.Message, state: FSMContext):
    try:
        amount = float(message.text.replace(",", "."))
        await state.update_data(amount=amount)
        await message.answer(
            f"Сумма: <b>{amount:.2f}</b>\n"
            "Теперь выбери валюту:"
        )
        await state.set_state(CurrencyConverter.from_currency)
    except ValueError:
        await message.answer("Введи число!")
