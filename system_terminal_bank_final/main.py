from modules.user_model import UserData
from modules.user_ui import operation_ui
from modules.login_system import login_or_create_user
from modules.user_model import Data_base

def start() -> None:
    user: UserData = login_or_create_user()

    operation_ui(user)

start()
