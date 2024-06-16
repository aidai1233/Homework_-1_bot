import aiosqlite
from database.queries import Queries


class Database:
    def __init__(self, path):
        self.path = path

    async def create_tables(self):
        async with aiosqlite.connect(self.path) as conn:
            try:
                # Создаем таблицу отзывов (review), если она еще не существует
                await conn.execute(Queries.CREATE_REVIEW_TABLE)
                await conn.commit()
                print("Таблица отзывов успешно создана или уже существует.")
            except aiosqlite.Error as e:
                print(f"Ошибка при создании таблицы отзывов: {e}")

    async def execute(self, query, params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            try:
                await conn.execute(query, params)
                await conn.commit()
                print("Запрос успешно выполнен.")
            except aiosqlite.Error as e:
                print(f"Ошибка выполнения запроса: {e}")

# Пример использования


async def main():
    db = Database('db.sqlite3')
    await db.create_tables()

    # Пример запроса INSERT для таблицы "review"
    query = "INSERT INTO db.sqlite3 (name, phone, date, food, cleanliness, comment) VALUES (?, ?, ?, ?, ?, ?)"
    params = ('Айдай', '0709331013', '12-09-2022', 'удовлетворительно', 'хорошо', 'очень уютно')
    await db.execute(query, params)

if __name__ == "__main__":
    import asyncio
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
