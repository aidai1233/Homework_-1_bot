from aiogram import Router, types, F
from aiogram.filters.command import Command
from config import database

menu_router = Router()


@menu_router.message(Command("menu"))
async def start_menu(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="Завтраки"),
                types.KeyboardButton(text="Паста")
            ],
            [
                types.KeyboardButton(text="Салаты"),
                types.KeyboardButton(text="Десерты")
            ]
        ],
        resize_keyboard=True
    )
    await message.answer("Выберите категорию:", reply_markup=kb)


categories = ("Завтраки", "Паста", "Салаты", "Десерты")


@menu_router.message(F.text.capitalize().in_(categories))
async def show_dishes_by_category(message: types.Message):
    kb = types.ReplyKeyboardRemove()
    category = message.text.capitalize()
    dishes = await database.fetch_all("""
        SELECT dishes.name, dishes.price 
        FROM dishes
        INNER JOIN categories ON dishes.category_id = categories.id
        WHERE categories.name = ?
    """, (category,))
    await message.answer(f"Блюда из категории {categories}", reply_markup=kb)

    for dish in dishes:
        message_text = f"{dish['name']} - {dish['price']} сом"
        await message.answer(message_text)
