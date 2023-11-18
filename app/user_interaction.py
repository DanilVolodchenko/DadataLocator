import dadata
import database
from validators import is_valid_language, is_valid_url_address, is_valid_api_key


def main_actions() -> None:
    while True:
        print('1. Ввести адрес')
        print('2. Обновить URL адрес или язык ответа')
        print('3. Изменить API ключ')
        print('0. Выход\n')

        choice = input('Выберите действие: ')

        if choice == '1':
            show_address()

        elif choice == '2':
            update_url_lang()

        elif choice == '3':
            update_api_key()

        elif choice == '0':
            break

        else:
            print('К сожалению, выбранного Вами действия нет, пожалуйста, попробуйте еще раз\n')


def show_address() -> None:
    """Выводит пользователю всевозможные адреса."""

    database.update_url_lang()

    query = input('Введите адрес: ')

    suggestions = dadata.get_list_of_addresses(query)
    results = dadata.get_value_of_addresses(suggestions)
    if results:
        print('**Выберете номер правильного адреса**')
        for i, result in enumerate(results, start=1):
            print(f'{i}. {result}')
        show_coordinate(results)

    else:
        print('Ничего не найдено')


def show_coordinate(results: list[str]) -> None:
    """Выводит пользователю координаты выбранного одреса."""

    try:
        number = int(input("Введите номер нужного адреса от 1 до 10: ").strip())

        full_address = results[number - 1]
        latitude, longitude = dadata.get_coordinates(full_address)

    except IndexError:
        print('Введите номер в диапазоне от 1 до 10\n')
    except ValueError:
        print('Нужно ввести только цифру\n')

    else:
        if latitude or longitude:
            print(f'Широта: {latitude}')
            print(f'Долгота: {longitude}\n')
        else:
            print('Извините, нет информации о координатах выбранного Вами адреса\n')


def create_api_key(db_api_key: str) -> None:
    """Добавляет API ключ в БД если такового нет."""

    while True:
        if db_api_key is None:
            api_key = input('Пожалуйста, введите API ключ для сервиса dadata: ')
            if is_valid_api_key(api_key):
                database.create_api_key(api_key)
                print('Ключ успешно добален.')
                break
            print('Введен неверный API ключ, пожалуйста, попробуйте еще раз\n')
        else:
            break


def update_api_key():
    """Обновляет данные API ключа в БД."""

    api_key = input('Пожалуйста, введите новый API ключ для сервиса dadata: ')
    if is_valid_api_key(api_key):
        database.update_api_key(api_key)
        print('Ключ успешно обновлен')
    print('Введен неверный API ключ, пожалуйста, попробуйте еще раз или выберете другое действие')


def update_url_lang():
    while True:
        print('1. Обновить URL адрес')
        print('2. Обновить язык ответа')
        print('0. Выход\n')

        choice = input('Выберите действие: ')

        if choice == '1':
            new_url = input('Введите URL адрес: ')
            if is_valid_url_address(new_url):
                database.update_base_url(new_url)
            else:
                print('Ввeден некорректный URL адрес')

        elif choice == '2':
            new_language = input('Выберите язык ответа (en/ru)')
            if is_valid_language(new_language):
                database.update_language(new_language)
            else:
                print('К сожалению, мы еще не умеем работать с выбранным Вами языком.')

        elif choice == '0':
            break

        else:
            print('К сожалению, выбранного Вами действия нет, пожалуйста, попробуйте еще раз')
