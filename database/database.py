import aiosqlite
from .queries import Queries


class Database:
    def __init__(self, path):
        self.path = path

    async def create_tables(self):
        async with aiosqlite.connect(self.path) as conn:
            async with conn.cursor() as cur:
                await cur.execute(Queries.CREATE_REVIEW_TABLE)
                await cur.execute(Queries.DROP_CATEGORIES_TABLE)
                await cur.execute(Queries.DROP_DISHES_TABLE)
                await cur.execute(Queries.CREATE_CATEGORIES_TABLE)
                await cur.execute(Queries.CREATE_DISHES_TABLE)
                await cur.execute(Queries.POPULATE_CATEGORY)
                await cur.execute(Queries.POPULATE_DISHES)
                await conn.commit()

    async def execute(self, query, params: tuple = ()):
        async with aiosqlite.connect(self.path) as conn:
            await conn.execute(query, params)
            await conn.commit()

