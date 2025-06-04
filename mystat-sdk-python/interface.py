from core import *

class MyStatApp:
        def __init__(self, login, password):
                self.login = login
                self.password = password
                self.token = None

        def auto(self):
                register, token = get_auth(self.login, self.password)
                if register:
                        self.token = token
                        print('успех')
                        with open('config.txt', 'w') as f:
                                f.write(token)

                else:
                        print('не успех')

        def marks(self):
                if not self.token:
                        print("сначала надо получить токен")
                        return
                marks = get_marks(self.login, self.password)
                if marks:
                        print('успех')
                        print(marks)
                else:
                        print('не успех')
