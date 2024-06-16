from aiogram import Router, types
from aiogram.filters.command import Command

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


menu_items = {
    "Завтраки": ["Омлет", "Блины", "Мюсли"],
    "Паста": ["Карбонара", "Болоньезе", "Альфредо"],
    "Салаты": ["Цезарь", "Греческий", "Овощной микс"],
    "Десерты": ["Тирамису", "Панна котта", "Чизкейк"]
}


@menu_router.message(lambda message: message.text in menu_items.keys())
async def menu_category(message: types.Message):
    category = message.text
    if category in menu_items:
        kb = types.ReplyKeyboardRemove()
        await message.answer(f"Блюда в категории \"{category}\":", reply_markup=kb)
        for item in menu_items[category]:
            await message.answer(f"- {item}")
    else:
        await message.answer("Выберите категорию из предложенных вариантов.")
