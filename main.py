from interface import MyStatApp

def main():
    print("авторизация в MyStat")
    login = input("введите логин: ")
    password = input("введите пароль: ")

    app = MyStatApp(login, password)

    while True:
        print("\nвыберите действие:")
        print("1. получить оценки")
        print("2. посчитать средний балл")
        print("3. посмотреть расписание")
        print("0. выход")
        choice = input(">> ")

        if choice == "1":
            app.marks()

        elif choice == "2":
            app.average_mark()

        elif choice == "3":
            week = input("показать неделю? (y/n): ").strip().lower() == 'y'
            date = input("введите дату в формате YYYY-MM-DD (или оставьте пустым): ").strip() or None
            app.show_schedule(week=week, date=date)

        elif choice == "0":
            print(" выход из приложения.")
            break

        else:
            print("неверный выбор. повторите попытку.")

if __name__ == "__main__":
    main()
