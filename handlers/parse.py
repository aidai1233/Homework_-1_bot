from aiogram import Router, types
from aiogram.fsm.context import FSMContext
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from crawler.house_kg import get_page, get_links

parse_router = Router()


@parse_router.message(Command("parse"))
async def start_parse(message: types.Message):
    kb = InlineKeyboardMarkup(inline_keyboard=[
        [InlineKeyboardButton(text="Спарсить объявления", callback_data="parse_house_kg")]
    ])
    await message.answer("Нажмите кнопку ниже, чтобы спарсить объявления:", reply_markup=kb)


@parse_router.callback_query(text="parse_house_kg", state="*")
async def parse_announcements(callback: CallbackQuery, state: FSMContext):
    page = get_page()
    links = get_links(page)

    await callback.message.answer("Ссылки на объявления:")
    for link in links:
        await callback.message.answer(link)
    await callback.answer()
