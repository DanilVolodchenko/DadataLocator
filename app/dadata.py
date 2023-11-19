from http import HTTPStatus

import requests

import database
from settings import NUMBER_OF_RESULT, DEFAULT_LANGUAGE, DEFAULT_URL_ADDRESS
from exceptions import CoordinatesNotFound, CoordinatesError


def get_list_of_addresses(query: str) -> dict[str, str]:
    """Возвращает список предполагаемых адресов."""

    data = database.get_data()

    response = get_response(query, *data)

    if response.status_code != HTTPStatus.OK:
        url_address, = database.get_url()
        print(url_address)
        raise requests.RequestException(
            f'Не получается отправить запрос по данному адресу: {url_address}'
        )
    return response.json().get('suggestions', [])


def get_value_of_addresses(suggestions: dict | None) -> list[str]:
    """Возвращает значения адресов."""

    return [sug.get("unrestricted_value") for sug in suggestions]


def get_coordinates(full_address: str) -> tuple[float, float]:
    """Возвращает координаты выбранного адреса."""

    data = database.get_data()

    response = get_response(full_address, *data, count=1)

    if response.status_code == HTTPStatus.OK:
        suggestions = response.json().get('suggestions', [])

        if suggestions:
            data = suggestions[0].get('data', {})
            coordinates = data.get('geo_lat'), data.get('geo_lon')
            return coordinates
        else:
            raise CoordinatesNotFound(
                f'Координаты для адреса: {full_address} не были найдены'
            )

    else:
        raise CoordinatesError('Ошибка получения координат')


def get_response(
        query: str, api_key: str,
        url_address: str = DEFAULT_URL_ADDRESS,
        language: str = DEFAULT_LANGUAGE,
        *, count: int = NUMBER_OF_RESULT
) -> requests.Response:
    """Возвращает ответ на запрос к dadata."""

    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'Authorization': f'Token {api_key}'
    }
    data = {
        'query': query,
        'language': language,
        'count': count
    }
    response = requests.post(url_address, headers=headers, json=data)
    return response
