class Queries:
    CREATE_REVIEW_TABLE = """
    CREATE TABLE IF NOT EXISTS review (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        phone TEXT,
        date TEXT,
        food TEXT,
        cleanliness TEXT,
        comment TEXT
    )
    """

    DROP_CATEGORIES_TABLE = "DROP TABLE IF EXISTS categories"
    DROP_DISHES_TABLE = "DROP TABLE IF EXISTS dishes"

    CREATE_CATEGORIES_TABLE = """
    CREATE TABLE IF NOT EXISTS categories (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT
    )
    """

    CREATE_DISHES_TABLE = """
    CREATE TABLE IF NOT EXISTS dishes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price NUMERIC,
        category_id INTEGER,
        FOREIGN KEY (category_id) REFERENCES categories(id)
    )
    """

    POPULATE_CATEGORY = """
    INSERT INTO categories (name)
    VALUES ('Завтраки'),
    ('Паста'),
    ('Салаты'),
    ('Десерты')
    """

    POPULATE_DISHES = """
    INSERT INTO dishes (name, price, category_id)
    VALUES ('Омлет', 180, 1),
    ('Блины', 250, 1),
    ('Мюсли', 200, 1),
    ('Карбонара', 400, 2),
    ('Болоньезе', 350, 2),
    ('Альфредо', 300, 2),
    ('Цезарь', 350, 3),
    ('Греческий', 200, 3),
    ('Овощной микс', 350, 3),
    ('Тирамису', 275, 4),
    ('Панна котта', 250, 4),
    ('Чизкейк', 300, 4)
    """
