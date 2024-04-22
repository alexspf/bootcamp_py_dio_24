from modules.utils import getpass
class UserData:
    def __init__(self, name: str, statement: float, history: list, password_crypt: str):
        self.name = name
        self.statement = statement
        self.history = history
        self.password_crypt = password_crypt

Data_base = UserData('alex', 10000, [], '1234')