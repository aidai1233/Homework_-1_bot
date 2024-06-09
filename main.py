import asyncio
from config import dp, bot
from handlers.start import start_router
from handlers.picture import picture_router
from handlers.myinfo import myinfo_router


async def main():
    dp.include_router(start_router)
    dp.include_router(picture_router)
    dp.include_router(myinfo_router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

