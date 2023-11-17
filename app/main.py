from app import dadata, database, user_interaction


def main():
    database.create_table()
    db_api_key = database.get_api_key()

    while True:
        # Проверка API ключа или добавление его в БД.
        if db_api_key is None:
            api_key = input('Пожалуйста, введите API ключ для сервиса dadata: ')
            # api_key = '0dab7075de0d47bca469b20e3e657d7963e46ecb'
            if dadata.check_api_key(api_key):
                database.create_api_key(api_key)
                return False
            print('Введен неверный API ключ, пожалуйста, попробуйте еще раз')

    while True:
        print('1. Ввести адрес')
        print('2. Обновить URL адрес или язык ответа')
        print('0. Выход')

        choice = input('Выберите действие: ')

        if choice == '1':

            user_interaction.input_address()

        elif choice == '2':
            user_interaction.change_url_lang()


        elif choice == '0':
            break

        else:
            print('К сожалению, выбранного Вами действия нет, выберите его из списка')


if __name__ == '__main__':
    main()
