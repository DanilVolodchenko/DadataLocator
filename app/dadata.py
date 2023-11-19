from http import HTTPStatus

import requests

import settings
import database


def get_list_of_addresses(query: str) -> dict[str, str]:
    """Возвращает список предполагаемых адресов."""

    response = get_response(query)

    if response.status_code == HTTPStatus.OK:
        return response.json().get('suggestions', [])
    else:
        print(f"Ошибка получения адресов: {response.status_code}, {response.text}")


def get_value_of_addresses(suggestions: dict) -> list[str]:
    """Возвращает значения адресов."""

    return [suggestion.get("unrestricted_value", {}) for suggestion in suggestions]


def get_coordinates(full_address: str) -> tuple[float, float]:
    """Возвращает координаты выбранного адреса."""

    response = get_response(full_address, count=1)

    if response.status_code == HTTPStatus.OK:
        suggestions = response.json().get('suggestions', [])

        if suggestions:
            data = suggestions[0].get('data', {})
            coordinates = data.get('geo_lat'), data.get('geo_lon')
            return coordinates
        else:
            print(f'Координаты не найдены для адреса: {full_address}')

    else:
        print(f"Ошибка получения координат: {response.status_code}, {response.text}")


def get_response(query: str, *, count: int = settings.DEFAULT_COUNT):
    """Возвращает ответ на запрос к dadata."""

    api_key, = database.get_api_key()

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Token {api_key}'
    }
    data = {
        'query': query,
        'language': settings.DEFAULT_LANGUAGE,
        'count': count
    }
    response = requests.post(settings.DEFAULT_BASE_URL, headers=headers, json=data)

    return response
