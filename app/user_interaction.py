import requests
import dadata
from utils import create_param_db, update_param_db
from exceptions import CoordinatesNotFound, CoordinatesError


def main_actions() -> None:
    """Основная работа с действиями пользователя."""

    while True:
        print('\n** Главное меню **\n'
              '1. Ввести нужный адрес\n'
              '2. Изменить URL адрес\n'
              '3. Изменить язык ответа\n'
              '4. Изменить API ключ\n'
              '0. Выход\n')

        choice = input('Выберите действие: ').strip()

        if choice == '1':
            show_address()

        elif choice == '2':
            update_url_address()

        elif choice == '3':
            update_language()

        elif choice == '4':
            update_api_key()

        elif choice == '0':
            break

        else:
            print('К сожалению, выбранного Вами действия нет, '
                  'пожалуйста, попробуйте еще раз\n')


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
            print('Ничего не найдено\n')


def create_api_key(db_api_key: str | None) -> None:
    """Добавляет API ключ в БД если такового нет."""

    while True:
        if db_api_key is None:
            api_key = input('\nПожалуйста, введите API ключ '
                            'для сервиса dadata: ')
            name = 'api_key'

            try:
                create_param_db(name, api_key)
            except (ValueError, TypeError):
                print('Введен неверный API ключ, '
                      'пожалуйста, попробуйте еще раз\n')
            else:
                print('Ключ успешно создан\n')
                break
        break


def show_coordinate(results: list[str]) -> None:
    """Выводит пользователю координаты выбранного одреса."""

    try:
        number = int(input('\nВведите номер нужного адреса'
                           ' от 1 до 10: ').strip())

        full_address = results[number - 1]
        latitude, longitude = dadata.get_coordinates(full_address)

    except IndexError:
        print('Введите номер в диапазоне от 1 до 10\n')

    except ValueError:
        print('Нужно ввести только цифру\n')

    except (CoordinatesNotFound, CoordinatesError) as ex:
        print(ex)

    else:
        if latitude or longitude:
            print('\n* Результат *\n'
                  f'Широта: {latitude}\n'
                  f'Долгота: {longitude}')
        else:
            print('Извините, нет информации о координатах '
                  'выбранного Вами адреса\n')


def update_api_key() -> None:
    """Обновляет данные API ключа в БД."""

    new_api_key = input('\nПожалуйста, введите новый API ключ '
                        'для сервиса dadata: ')
    name = 'api_key'
    try:
        update_param_db(name, new_api_key)
    except (ValueError, TypeError):
        print('\nВведен неверный API ключ, пожалуйста, '
              'попробуйте еще раз или выберете другое действие\n')
    else:
        print('* Ключ успешно обновлен *\n')


def update_url_address() -> None:
    """Обновляет URL адрес."""

    new_url = input('\nВведите URL адрес: ')
    name = 'url_address'

    try:
        update_param_db(name, new_url)
    except (ValueError, TypeError):
        print('\nВвeден некорректный URL адрес\n')
    else:
        print('* URL адрес успешно изменен *\n')


def update_language() -> None:
    """Обновляет язык ответа."""

    new_language = input('\nВыберите язык ответа (en/ru) ')
    name = 'language'

    try:
        update_param_db(name, new_language)
    except (ValueError, TypeError):
        print('\nК сожалению, мы еще не умеем работать с '
              'выбранным Вами языком\n')
    else:
        print('* Язык ответа успешно изменен *\n')
