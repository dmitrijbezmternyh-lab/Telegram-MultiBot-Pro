from aiogram import Router, types, F
from aiogram.filters import Command
from bot.services.gpt import GPTService
from collections import defaultdict

router = Router()
gpt_service = GPTService()
user_contexts = defaultdict(list)

@router.message(F.text == "Assistent")
@router.message(Command("ast"))
async def gpt_start(message: types.Message):
    user_contexts[message.from_user.id] = []
    await message.answer(
        " <b>Режим Assistent активирован!</b>\n\n"
        "Задавай вопросы, я постараюсь помочь.\n"
        "Для выхода нажми  Главное меню\n\n"
        " <i>Контекст сохраняется (15 сообщений)</i>"
    )

@router.message(F.text.startswith("/gpt "))
async def gpt_command(message: types.Message):
    question = message.text[5:]
    await message.answer(" Думаю...")
    
    response = await gpt_service.ask(message.from_user.id, question)
    await message.answer(response)

@router.message(lambda msg: msg.from_user.id in user_contexts)
async def gpt_dialog(message: types.Message):
    if message.text in ["Главное меню", "/start"]:
        del user_contexts[message.from_user.id]
        return
    
    await message.bot.send_chat_action(message.chat.id, "typing")
    response = await gpt_service.ask(message.from_user.id, message.text)
    await message.answer(response)
