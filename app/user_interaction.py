from app import database


def input_address():
    database.create_url_lang()

    query = input('Введите адрес: ')


def check_language(language):
    if language.lower() in ('ru', 'en'):
        database.update_language(language)


def change_url_lang():
    print('1. Хочу обновить URL адрес')
    print('2. Хочу обновить язык ответа')
    print('3. Хочу обновить URL адрес и язык ответа')

    choice = input('Выберите действие: ')

    if choice == '1':
        new_url = input('Введите URL адрес: ')
        database.update_base_url(new_url)

    elif choice == '2':
        new_language = input('Выберите язык ответа (en/ru)')
        if new_language.lower() in ('ru', 'en'):
            database.update_language(new_language)
        else:
            print('К сожалению, мы еще не умеем работать с выбранным Вами языком.')

    elif choice == '3':
        while True:
            try:
                new_url, new_language = input('Введите URL адрес и язык ответа через пробел').split()
                database.update_base_url(new_url)
                database.update_language(new_language)
                break

            except ValueError:
                print('Введите ')


a, b = 'asdffa'.split()

# print(a.split())
