import sqlite3

from settings import DEFAULT_BASE_URL, DEFAULT_LANGUAGE

connect = sqlite3.connect('../db_settings.sqlite3')
cursor = connect.cursor()


def create_table() -> None:
    """Создает таблицу в БД."""

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            api_key TEXT,
            base_url TEXT,
            language TEXT
        )
    """)
    connect.commit()


def get_data() -> tuple[str]:
    """Возвращает данные из БД."""

    cursor.execute("SELECT * FROM settings")
    return cursor.fetchone()


def get_api_key() -> tuple[str]:
    """Возвращает API ключ из БД."""

    cursor.execute('SELECT api_key FROM settings WHERE ROWID=1')
    # api_key, = cursor.fetchone()
    return cursor.fetchone()


def get_url() -> str:
    """Возвращает url адрес из БД."""

    cursor.execute('SELECT base_url FROM settings')
    url, = cursor.fetchone()
    return url


def get_language() -> str:
    """Возвращает язык ответа из БД."""

    cursor.execute('SELECT language FROM settings')
    language, = cursor.fetchone()
    return language


def update_url_lang(url: str = DEFAULT_BASE_URL, language: str = DEFAULT_LANGUAGE) -> None:
    """Добаляет url и language в БД."""

    cursor.execute(
        """UPDATE settings SET base_url=?, language=? WHERE ROWID=1""",
        (url, language)
    )
    connect.commit()


def create_api_key(api_key: str) -> None:
    """Создает API KEY пользователя."""

    cursor.execute(
        "INSERT INTO settings (api_key) VALUES (?)",
        (api_key,)
    )
    connect.commit()


def update_base_url(url: str) -> None:
    """Обновляет данные url в БД."""

    cursor.execute(
        """UPDATE settings SET base_url=? WHERE ROWID=1""",
        (url,)
    )
    connect.commit()


def update_language(language: str) -> None:
    """Обновляет данные language в БД."""

    cursor.execute(
        """UPDATE settings SET language=? WHERE ROWID=1""",
        (language,)
    )
    connect.commit()


def update_api_key(api_key: str) -> None:
    """Обновляет данные API ключа в БД."""

    cursor.execute(
        """UPDATE settings SET api_key=? WHERE ROWID=1""",
        (api_key,)
    )
    connect.commit()
