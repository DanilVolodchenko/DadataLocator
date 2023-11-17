from http import HTTPStatus

import requests

import settings
import database


def check_api_key(api_key):
    """Проверяет API ключ на корректность."""

    if len(api_key) != settings.DEFAULT_API_KEY_LENGTH:
        return False

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Token {api_key}'
    }
    data = {
        'query': 'Новосибирск',
    }
    response = requests.post(settings.DEFAULT_BASE_URL, headers=headers, json=data)
    if response.status_code == HTTPStatus.OK:
        return True
    return False


def get_addresses(query):
    """Возвращает полученные адреса."""

    api_key = database.get_api_key()

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Token {api_key}'
    }
    data = {
        'query': 'Новосибирск кос',
        'language': settings.DEFAULT_LANGUAGE
    }

    response = requests.post(settings.DEFAULT_BASE_URL, headers=headers, json=data)
    if response.status_code == HTTPStatus.OK:
        print(response.json()['suggestions'])
    else:
        print(f"Ошибка получения предложений адресов: {response.status_code}, {response.text}")
