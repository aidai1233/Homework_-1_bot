class Queries:
    CREATE_REVIEW_TABLE = """
    CREATE TABLE IF NOT EXISTS review (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        phone TEXT NOT NULL,
        visit_date TEXT NOT NULL,
        food_quality TEXT NOT NULL,
        cleanliness TEXT NOT NULL,
        comments TEXT
    );
    """
