from aiogram import Router, types
from aiogram.filters.command import Command


myinfo_router = Router()


@myinfo_router.message(Command("myinfo"))
async def myinfo_handler(message: types.Message):
    await message.answer(
        f"Ваш ID: {message.from_user.id}, Имя: {message.from_user.first_name}, Ник: {message.from_user.username}"
    )
