from aiogram import types, Router, F
from aiogram.filters.command import Command
from aiogram.fsm.context import FSMContext
from handlers.survey import start_survey
from handlers.menu import start_menu

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
                types.InlineKeyboardButton(text="Меню", callback_data="menu")
            ],
            [
                types.InlineKeyboardButton(text="Оставить отзыв", callback_data="survey")
            ]
        ]
    )

    name = message.from_user.first_name
    await message.answer(f"Привет, {name}",
                         reply_markup=keyboard)


@start_router.callback_query(F.data == "menu")
async def menu_handler(callback: types.CallbackQuery):
    await start_menu(callback.message)
    await callback.answer()


@start_router.callback_query(F.data == "survey")
async def survey_handler(callback: types.CallbackQuery, state: FSMContext):
    await start_survey(callback.message, state)
    await callback.answer()


