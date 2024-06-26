import asyncio
import logging
from aiogram import types
from config import dp, bot
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.myinfo import myinfo_router
from handlers.survey import survey_router
from handlers.menu import menu_router
from database.database import Database
from handlers.parse import parse_router

database = Database("db.sqlite")


async def on_startup(bot):
    await database.create_tables()


async def main():
    await bot.set_my_commands([
        types.BotCommand(command="start", description="Начало"),
        types.BotCommand(command="menu", description="Меню"),
        types.BotCommand(command="opros", description="Пройдите на опрос"),
        types.BotCommand(command="parse", description="Начать парсинг объявлений")
    ])

    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(myinfo_router)
    dp.include_router(survey_router)
    dp.include_router(menu_router)
    dp.include_router(parse_router)
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())

