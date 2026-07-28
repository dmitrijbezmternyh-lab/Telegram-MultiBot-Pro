import asyncio
import structlog
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage

from bot.config import config
from bot.middlewares.logging import LoggingMiddleware
from bot.middlewares.throttling import ThrottlingMiddleware
from bot.handlers import start, weather, currency, chatgpt, admin, qrcode_handler, fun
from bot.services.database import Database

logger = structlog.get_logger()

async def main():
    # Конфигурация
    config.validate()
    
    # Инициализация
    bot = Bot(token=config.BOT_TOKEN, parse_mode="HTML")
    storage = MemoryStorage()
    dp = Dispatcher(storage=storage)
    db = Database(config.DATABASE_URL)
    await db.init()
    
    # Middleware
    dp.message.middleware(LoggingMiddleware())
    dp.message.middleware(ThrottlingMiddleware(config.RATE_LIMIT))
    dp.callback_query.middleware(LoggingMiddleware())
    
    # Регистрация роутеров
    dp.include_router(start.router)
    dp.include_router(weather.router)
    dp.include_router(currency.router)
    dp.include_router(chatgpt.router)
    dp.include_router(admin.router)
    dp.include_router(qrcode_handler.router)
    dp.include_router(fun.router)
    
    # Запуск
    logger.info("Bot started")
    await dp.start_polling(bot, db=db)

if __name__ == "__main__":
    asyncio.run(main())
