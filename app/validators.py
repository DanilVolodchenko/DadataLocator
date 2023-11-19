import re
from http import HTTPStatus

from dadata import get_response


def is_valid_api_key(api_key: str) -> bool:
    """Проверяет API ключ на корректность."""

    query = 'Какой-то запрос'
    response = get_response(query, api_key)

    return response.status_code == HTTPStatus.OK


def is_valid_language(language: str) -> bool:
    """Проверка введенного языка на корректность."""

    return language.lower() in ('ru', 'en')


def is_valid_url_address(url_address: str) -> bool:
    """Проверка введенного URL адресса на корректность."""

    url_pattern = re.compile(
        r'^(?:http|https)://'
        r'(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+'
        r'(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)/?'
        r'[^/\s]+(?:/[^/\s]*)*$', re.IGNORECASE)

    return bool(re.match(url_pattern, url_address))
