from core import *

class MyStatApp:
        def __init__(self, login, password):
                self.login = login
                self.password = password
                self.token = get_auth(self.login, self.password)[1]

        def marks(self):
                if not self.token:
                        print("сначала надо получить токен")
                        return
                marks = get_marks(self.token)
                if marks:
                        print('успех, вы получили токен')
                else:
                        print('не успех')

        def average_mark(self):
                if self.token:
                        avg = calc_avr_mark(self.token)
                        if avg:
                                print(f"ваш средний балл: {avg}")
                        else:
                                print("оценки не найдены")
                else:
                        print("токен не получен")

        def show_schedule(self, week = True, date = None):
                if not self.token:
                        print("сначала нужно авторизоваться.")
                        return
                schedule = get_schedule(self.token, week=week, date=date)
                if schedule:
                        for i in schedule:
                                print(f"{i['date']} - {i['title']}")
                else:
                        print("расписание не получено.")
                

                        
