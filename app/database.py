import sqlite3

from settings import DEFAULT_BASE_URL, DEFAULT_LANGUAGE


connect = sqlite3.connect('../db_settings.sqlite3')
cursor = connect.cursor()


def create_table():
    """Создает таблицу в БД."""

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            api_key TEXT,
            base_url TEXT,
            language TEXT
        )
    """)
    connect.commit()


def get_data():
    """Возвращает данные из БД."""

    cursor.execute("SELECT * FROM settings")
    return cursor.fetchone()


def get_api_key():
    """Возвращает API ключ из БД."""

    cursor.execute('SELECT api_key FROM settings')
    return cursor.fetchone()


def get_url():
    """Возвращает url адрес из БД."""

    cursor.execute('SELECT base_url FROM settings')
    return cursor.fetchone()


def get_language():
    """Возвращает язык ответа из БД."""

    cursor.execute('SELECT language FROM settings')
    return cursor.fetchone()


def create_url_lang(url=DEFAULT_BASE_URL, language=DEFAULT_LANGUAGE):
    """Добаляет url и language в БД."""

    cursor.execute(
        "INSERT INTO settings (base_url, language) VALUES (?, ?)",
        (url, language)
    )
    connect.commit()


def create_api_key(api_key):
    """Создает API KEY пользователя."""

    cursor.execute(
        "INSERT INTO settings (api_key) VALUES (?)",
        (api_key,)
    )
    connect.commit()


def update_base_url(url):
    """Обновляет данные url в БД."""

    cursor.execute(
        """UPDATE settings SET base_url=?""",
        (url,)
    )
    connect.commit()


def update_language(language):
    """Обновляет данные language в БД."""

    cursor.execute(
        """UPDATE settings SET language=?""",
        (language,)
    )
    connect.commit()
