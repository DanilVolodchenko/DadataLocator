import database
import user_interaction


def main() -> None:
    try:
        database.create_table()
        api_key, = database.get_api_key()

        user_interaction.create_api_key(api_key)
        user_interaction.main_actions()

    except Exception as ex:
        print(f'Упс, произошла ошибка: {ex}')


if __name__ == '__main__':
    main()
