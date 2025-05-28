import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from core.config import Settings
from core.router_manager import setup_router
from logger.logger import get_logger
from services.weather import get_weather

async def main():
    logger = get_logger('MyBot')
    logger.info("Бот запущен")
    logger.error("Произошла ошибка")
    logger.error("Starting bot")
    
    config = Settings()
    router = setup_router()
    
    bot = Bot(token=config.bot_token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher(config=config)
    dp.include_routers(router)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

def cli():
    try:
        asyncio.run(main())
    except (KeyboardInterrupt, SystemExit):
        get_logger.error("Bot stopped!")


if __name__ == '__main__':
    cli()