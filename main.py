import asyncio
import random
import os
from aiogram import Bot, Dispatcher, types
from aiogram.filters.command import Command
from dotenv import load_dotenv
from os import getenv
from aiogram.types import FSInputFile

load_dotenv()
bot = Bot(token=getenv('BOT_TOKEN'))
dp = Dispatcher()


@dp.message(Command("start"))
async def start_handler(message: types.Message):
    print("start command")
    name = message.from_user.first_name
    await message.answer(f"Привет, {name}")


@dp.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    await message.answer(
        f"Ваш ID: {message.from_user.id}, Имя: {message.from_user.first_name}, Ник: {message.from_user.username}"
    )


@dp.message(Command("picture"))
async def picture_handler(message: types.Message):
    images_folder = r'C:\Users\Notnik_kg\PycharmProjects\домашки 3 месяца\images'
    images = os.listdir(images_folder)
    random_image = random.choice(images)
    file = FSInputFile(images_folder + random_image)
    await message.answer_photo(file)


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())

