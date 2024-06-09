from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.types import FSInputFile


start_router = Router()


@start_router.message(Command("start"))
async def start_handler(message: types.Message):
    print("start command")
    keyboard = types.InlineKeyboardMarkup(
        inline_keyboard=[
            [
                types.InlineKeyboardButton(text="Наш инстаграм", url="https://www.instagram.com/panfiloff_bishkek")
            ],
            [
                types.InlineKeyboardButton(text="Наш адрес", url="https://2gis.kg/bishkek/firm/70000001050087092"),
                types.InlineKeyboardButton(text="Контакты", url="https://api.whatsapp.com/send/?phone=996700250000")
            ],
            [
                types.InlineKeyboardButton(text="Отзывы",
                                           url="https://2gis.kg/bishkek/firm/70000001050087092/tab/reviews")
            ],
            [
                types.InlineKeyboardButton(text="Меню", callback_data="reply_photo")
            ],
        ]
    )

    name = message.from_user.first_name
    await message.answer(f"Привет, {name}",
                         reply_markup=keyboard)


@start_router.callback_query(F.data == "reply_photo")
async def reply_photo_handler(callback: types.CallbackQuery):
    file = FSInputFile("menu/меню.PNG")
    await callback.message.reply_photo(photo=file, caption="Меню")
    await callback.answer()