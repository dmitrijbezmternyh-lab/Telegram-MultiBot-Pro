from aiogram import Router, types, F
from aiogram.filters import Command
import random

router = Router()

EASTER_EGGS = {
    "пасхалка": "Ты нашел пасхалку!",
    "42": "Ответ на главный вопрос жизни, вселенной и всего такого",
    "кот": "Мяу!",
}

@router.message(F.text == "Игры")
@router.message(Command("game"))
async def game_menu(message: types.Message):
    await message.answer(
        "<b>Мини-игры</b>\n\n"
        " Бросить кубик - /dice\n"
        " Дартс - /darts\n"
        " Слоты - /slots\n"
        " Баскетбол - /basket\n"
        " Боулинг - /bowl\n"
        " Монетка - /coin"
    )

@router.message(Command("dice"))
async def cmd_dice(message: types.Message):
    await message.answer_dice(emoji="[:]")

@router.message(Command("coin"))
async def cmd_coin(message: types.Message):
    result = random.choice(["Орел", "Решка"])
    await message.answer(f"<b>Монетка:</b> {result}")

@router.message(lambda msg: msg.text.lower() in EASTER_EGGS)
async def easter_eggs(message: types.Message):
    await message.answer(EASTER_EGGS[message.text.lower()])

@router.message(Command("joke"))
async def cmd_joke(message: types.Message):
    jokes = [
        "Почему программисты не ходят в лес? Там нет Wi-Fi!",
        "Как назвать программиста на пляже? Байт-код!",
        "Что говорит один сервер другому? Ты меня пингуешь?",
    ]
    await message.answer(f"{random.choice(jokes)}")
