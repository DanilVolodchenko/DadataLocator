import sqlite3

from settings import DEFAULT_BASE_URL, DEFAULT_LANGUAGE, DEFAULT_DB_FILE


def execute_query(query: str, parameters: tuple = ()) -> None:
    """Выполняет различные запросы."""

    with sqlite3.connect(DEFAULT_DB_FILE) as connect:
        cursor = connect.cursor()
        try:
            cursor.execute(query, parameters)
        except sqlite3.Error as er:
            print(f'Произошла ошибка с БД {er}')

        connect.commit()


def execute_return_query(query: str) -> str:
    """Выполняет запрос и возвращает результат."""

    with sqlite3.connect(DEFAULT_DB_FILE) as conn:
        cursor = conn.cursor()
        cursor.execute(query)

        return cursor.fetchone()


def create_table() -> None:
    """Создает таблицу в БД."""

    query = f"""
                CREATE TABLE IF NOT EXISTS settings (
                    api_key TEXT,
                    base_url TEXT DEFAULT '{DEFAULT_BASE_URL}',
                    language TEXT DEFAULT '{DEFAULT_LANGUAGE}'
                )
            """

    execute_query(query)


def get_api_key() -> str:
    """Возвращает API ключ из БД."""

    query = 'SELECT api_key FROM settings WHERE ROWID=1'

    return execute_return_query(query)


def get_language() -> str:
    """Возвращает язык ответа."""

    query = 'SELECT language FROM settings WHERE ROWID=1'

    return execute_return_query(query)


def update_url_lang(url: str = DEFAULT_BASE_URL, language: str = DEFAULT_LANGUAGE) -> None:
    """Добаляет url и language в БД."""

    query = "UPDATE settings SET base_url=?, language=? WHERE ROWID=1"
    parameters = (url, language)

    execute_query(query, parameters)


def create_api_key(api_key: str) -> None:
    """Создает API KEY пользователя."""

    query = "INSERT INTO settings (api_key) VALUES (?)"
    parameters = (api_key,)

    execute_query(query, parameters)


def update_base_url(url: str) -> None:
    """Обновляет данные url в БД."""

    query = "UPDATE settings SET base_url=? WHERE ROWID=1"
    parameters = (url,)

    execute_query(query, parameters)


def update_language(language: str) -> None:
    """Обновляет данные language в БД."""

    query = "UPDATE settings SET language=? WHERE ROWID=1"
    parameters = (language,)

    execute_query(query, parameters)


def update_api_key(api_key: str) -> None:
    """Обновляет данные API ключа в БД."""

    query = "UPDATE settings SET api_key=? WHERE ROWID=1"
    parameters = (api_key,)

    execute_query(query, parameters)
