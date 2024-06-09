from aiogram import Router, types
from aiogram.types import FSInputFile
import random
import os
from aiogram.filters.command import Command


picture_router = Router()


@picture_router.message(Command("picture"))
async def picture_handler(message: types.Message):
    images_folder = 'images'
    images = os.listdir(images_folder)
    random_image = random.choice(images)
    file_path = os.path.join(images_folder, random_image)
    file = FSInputFile(file_path)
    await message.answer_photo(photo=file, caption="Сегодня отличный день для новых вкусовых открытий! "
                                                   "Чтобы поднять настроение, попробуйте это:")
