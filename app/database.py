import sqlite3

from settings import DEFAULT_URL_ADDRESS, DEFAULT_LANGUAGE, DEFAULT_DB_FILE


def execute_query(query: str, parameters: tuple = ()) -> None:
    """Выполняет различные запросы."""

    with sqlite3.connect(DEFAULT_DB_FILE) as connect:
        cursor = connect.cursor()
        try:
            cursor.execute(query, parameters)
        except sqlite3.Error as er:
            print(f'Произошла ошибка с БД {er}')

        connect.commit()


def execute_return_query(query: str) -> tuple[str]:
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
                    url_address TEXT DEFAULT '{DEFAULT_URL_ADDRESS}',
                    language TEXT DEFAULT '{DEFAULT_LANGUAGE}'
                )
            """

    execute_query(query)


def get_data() -> tuple[str]:
    """
    Возвращает запись о настройке пользователя из БД.
    """
    query = 'SELECT * FROM settings WHERE ROWID=1'

    return execute_return_query(query)


def get_api_key() -> tuple[str]:
    """Возвращает API ключ из БД."""

    query = 'SELECT api_key FROM settings WHERE ROWID=1'

    return execute_return_query(query)


def get_language() -> tuple[str]:
    """Возвращает язык ответа из БД."""

    query = 'SELECT language FROM settings WHERE ROWID=1'

    return execute_return_query(query)


def get_url() -> tuple[str]:
    """Возвращает URL адрес из БД."""

    query = 'SELECT url_address FROM settings WHERE ROWID=1'

    return execute_return_query(query)


def create_api_key(api_key: str) -> None:
    """Создает API KEY пользователя."""

    query = "INSERT INTO settings (api_key) VALUES (?)"
    parameters = (api_key,)

    execute_query(query, parameters)


def update_url_address(url: str) -> None:
    """Обновляет данные url в БД."""

    query = "UPDATE settings SET url_address=? WHERE ROWID=1"
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
