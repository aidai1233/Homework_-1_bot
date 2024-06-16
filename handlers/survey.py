from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram import types, Router
from aiogram.filters.command import Command
from datetime import datetime
import re
from database.database import Database

db = Database("db.sqlite3")
survey_router = Router()


class Survey(StatesGroup):
    name = State()
    phone = State()
    date = State()
    food = State()
    cleanliness = State()
    comment = State()


@survey_router.message(Command("opros"))
async def start_survey(message: types.Message, state: FSMContext):
    await state.set_state(Survey.name)
    await message.answer("Чтобы оставить отзыв вы должны пройти опрос. \n Как вас зовут?")


def is_cyrillic(text):
    pattern = r'^[А-ЯЁ][а-яё]+$'
    return re.match(pattern, text) is not None


@survey_router.message(Survey.name)
async def process_name(message: types.Message, state: FSMContext):
    if is_cyrillic(message.text):
        await state.update_data(name=message.text)
        await state.set_state(Survey.phone)
        await message.answer("Ваш номер телефона?")
    else:
        await message.answer("Пожалуйста, введите имя на кириллице и с заглавной буквой.")


@survey_router.message(Survey.phone)
async def process_phone(message: types.Message, state: FSMContext):
    await state.update_data(phone=message.text)
    await state.set_state(Survey.date)
    await message.answer("Дата вашего посещения нашего заведения? (дд-мм-гггг)")


def is_valid_date(date_str):
    try:
        datetime.strptime(date_str, "%d-%m-%Y")
        return True
    except ValueError:
        return False


@survey_router.message(Survey.date)
async def process_date(message: types.Message, state: FSMContext):
    if not is_valid_date(message.text):
        await message.answer("Пожалуйста, введите дату в формате дд-мм-гггг:")
        return
    await state.update_data(date=message.text)
    await state.set_state(Survey.food)
    await message.answer("Как оцениваете качество еды?", reply_markup=get_food_keyboard())


def get_food_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="плохо"),
                types.KeyboardButton(text="удовлетворительно")
            ],
            [
                types.KeyboardButton(text="хорошо"),
                types.KeyboardButton(text="отлично")
            ]
        ],
        resize_keyboard=True
    )


@survey_router.message(Survey.food)
async def process_food(message: types.Message, state: FSMContext):
    if message.text.lower() in ["плохо", "удовлетворительно", "хорошо", "отлично"]:
        await state.update_data(food=message.text)
        await message.answer(f"Спасибо за ваш отзыв по качеству еды: {message.text}")
        await state.set_state(Survey.cleanliness)
        await message.answer("Как оцениваете чистоту заведения?", reply_markup=get_cleanliness_keyboard())
    else:
        await message.answer("Пожалуйста, выберите один из вариантов: плохо, удовлетворительно, хорошо, отлично.",
                             reply_markup=get_food_keyboard())


def get_cleanliness_keyboard():
    return types.ReplyKeyboardMarkup(
        keyboard=[
            [
                types.KeyboardButton(text="плохо"),
                types.KeyboardButton(text="удовлетворительно")
            ],
            [
                types.KeyboardButton(text="хорошо"),
                types.KeyboardButton(text="отлично")
            ]
        ],
        resize_keyboard=True
    )


@survey_router.message(Survey.cleanliness)
async def process_cleanliness(message: types.Message, state: FSMContext):
    if message.text.lower() in ["плохо", "удовлетворительно", "хорошо", "отлично"]:
        await state.update_data(cleanliness=message.text)
        await message.answer(f"Спасибо за ваш отзыв по чистоте заведения: {message.text}")
        await state.set_state(Survey.comment)
        await message.answer("Ваши дополнительные комментарии (можете ввести много текста):")
    else:
        await message.answer("Пожалуйста, выберите один из вариантов: плохо, удовлетворительно, хорошо, отлично.",
                             reply_markup=get_cleanliness_keyboard())


@survey_router.message(Survey.comment)
async def process_comments(message: types.Message, state: FSMContext):
    await state.update_data(comment=message.text)
    data = await state.get_data()
    print("Data", data)
    await db.execute(
        "INSERT INTO review (name, phone, date, food,"
        " cleanliness, comment) VALUES (?, ?, ?, ?, ?, ?)",
        (data['name'], data['phone'], data['date'], data['food'], data['cleanliness'], data['comment'])
    )
    await state.clear()
    await message.answer("Спасибо за прохождение опроса", reply_markup=types.ReplyKeyboardRemove())
