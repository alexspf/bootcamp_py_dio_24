from modules.utils import os

def get_erro():
    print('Invalid option. Please try again.')
    os.system('clear')

def get_value(option):

    match option:    
        case 1:
            return float(input('How much do you want to deposit? $'))

        case 2:
            return float(input('How much do you want to withdraw? $'))
        