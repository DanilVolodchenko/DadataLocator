from database import (update_language, update_url_address,
                      update_api_key, create_api_key)
from validators import (is_valid_language, is_valid_url_address,
                        is_valid_api_key)


def create_param_db(name: str, value: str) -> None:
    """Создает запись в БД."""

    actions = {'api_key': [is_valid_api_key, create_api_key]}
    is_valid, create_value = actions.get(name)

    if is_valid(value):
        create_value(value)
    else:
        raise ValueError


def update_param_db(name: str, value: str) -> None:
    """Обновляет запись в БД."""

    actions = {'language': [is_valid_language, update_language],
               'url_address': [is_valid_url_address, update_url_address],
               'api_key': [is_valid_api_key, update_api_key]}
    is_valid, update_value = actions.get(name)

    if is_valid(value):
        update_value(value)
    else:
        raise ValueError
