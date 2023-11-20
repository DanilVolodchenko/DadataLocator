import requests
import dadata
from utils import create_param_db, update_param_db
from exceptions import CoordinatesNotFound, CoordinatesError


def main_actions() -> None:
    """Основная работа с действиями пользователя."""

    while True:
        print('\n** Главное меню **\n'
              '1. Ввести нужный адрес\n'
              '2. Выбрать язык ответа\n'
              '3. Изменить URL адрес\n'
              '4. Изменить API-ключ\n'
              '0. Выход\n')

        actions = {
            '1': show_address,
            '2': update_language,
            '3': update_url_address,
            '4': update_api_key,
        }

        choice = input('Выберите действие: ').strip()

        if choice == '0':
            break

        action = actions.get(choice, None)
        if action:
            action()

        else:
            print('К сожалению, выбранного вами действия нет, '
                  'пожалуйста, попробуйте еще раз')


def show_address() -> None:
    """Выводит пользователю всевозможные адреса."""

    query = input('\nВведите адрес: ')

    try:
        suggestions = dadata.get_list_of_addresses(query)
        addresses = dadata.get_value_of_addresses(suggestions)

    except requests.RequestException as ex:
        print(ex)

    else:
        if addresses:
            print('\n* Найденные адреса *')
            for i, result in enumerate(addresses, start=1):
                print(f'{i}. {result}')
            show_coordinate(addresses)

        else:
            print('Ничего не найдено, пожалуйста, попробуйте еще раз')


def show_coordinate(results: list[str]) -> None:
    """Выводит пользователю координаты выбранного одреса."""

    try:
        number = int(input('\nВведите номер нужного адреса'
                           f' от 1 до {len(results)}: ').strip())

        if number < 1 or number > len(results):
            raise IndexError

        full_address = results[number - 1]
        latitude, longitude = dadata.get_coordinates(full_address)

    except IndexError:
        print('\nНужно ввести цифру диапазоне '
              f' от 1 до {len(results)}: ')

    except ValueError:
        print('Ввести нужно только цифру\n')

    except (CoordinatesNotFound, CoordinatesError) as ex:
        print(ex)

    else:
        if latitude or longitude:
            print('\n* Результат *\n'
                  f'Широта: {float(latitude)}\n'
                  f'Долгота: {float(longitude)}')
        else:
            print('Извините, нет информации о координатах '
                  'выбранного вами адреса\n')


def create_api_key(db_api_key: tuple[str] | None) -> None:
    """Добавляет API-ключ в БД если такового нет."""

    while True:
        if db_api_key is None:
            api_key = input('\nПожалуйста, введите API-ключ '
                            'для сервиса dadata: ')
            name = 'api_key'

            try:
                create_param_db(name, api_key)
            except (ValueError, TypeError):
                print('Введен неверный API-ключ, '
                      'пожалуйста, попробуйте еще раз')
            else:
                print('* Ключ успешно создан *')
                break
        else:
            break


def update_api_key() -> None:
    """Обновляет данные API-ключа в БД."""

    new_api_key = input('\nПожалуйста, введите новый API-ключ '
                        'для сервиса dadata: ')
    name = 'api_key'
    try:
        update_param_db(name, new_api_key)
    except (ValueError, TypeError):
        print('\nВведен неверный API-ключ, пожалуйста, '
              'попробуйте еще раз')
    else:
        print('* Ключ успешно обновлен *')


def update_url_address() -> None:
    """Обновляет URL адрес."""

    new_url = input('\nВведите URL адрес: ')
    name = 'url_address'

    try:
        update_param_db(name, new_url)
    except (ValueError, TypeError):
        print('\nВвeден некорректный URL адрес, пожалуйста, '
              'попробуйте еще раз')
    else:
        print('* URL адрес успешно изменен *')


def update_language() -> None:
    """Обновляет язык ответа."""

    new_language = input('\nВыберите язык ответа (en/ru) ')
    name = 'language'

    try:
        update_param_db(name, new_language)
    except (ValueError, TypeError):
        print('\nК сожалению, мы еще не умеем работать с '
              'выбранным вами языком')
    else:
        print('* Язык ответа успешно изменен *')
