from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import FSInputFile
from bot.services.qrcode_generator import QRCodeGenerator

router = Router()

@router.message(F.text == "QR-код")
@router.message(Command("qrcode"))
async def qrcode_start(message: types.Message):
    await message.answer(
        "<b>Генератор QR-кодов</b>\n\n"
        "Отправь мне текст или ссылку, и я создам QR-код.\n"
        "Пример: /qrcode https://github.com"
    )

@router.message(Command("qrcode"))
async def qrcode_command(message: types.Message):
    text = message.text.split(" ", 1)[1] if len(message.text.split()) > 1 else None
    
    if not text:
        await message.answer("Укажи текст после команды!\nПример: /qrcode Привет!")
        return
    
    await message.bot.send_chat_action(message.chat.id, "upload_photo")
    
    qr_image = QRCodeGenerator.generate(text)
    
    if qr_image:
        photo = FSInputFile(qr_image)
        await message.answer_photo(
            photo,
            caption=f"QR-код для:\n<code>{text[:100]}</code>"
        )
    else:
        await message.answer(" Ошибка при создании QR-кода")
