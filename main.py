from scripts import *
from time import sleep
import os
import glob


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


def main():

    clear()

    path = 'scripts/'
    scripts = {}

    i = 1

    try:
        os.chdir(path)
    except EnvironmentError:
        pass

    for file in glob.glob('*.py'):
        if not file == '__init__.py':
            modules = file.replace('.py', '')
            scripts[i] = modules
            i += 1
    user_input(scripts)


def user_input(scripts):

    clear()

    for key, value in scripts.items():
        print(key, "=", value)

    try:
        x = int(input())

        if x in scripts:
            eval(scripts[x]+".main()")
        else:
            print('Value does not exist. Try again.')
            sleep(2)
            user_input(scripts)

    except ValueError:
        clear()
        print('Input is not an integer, dumbass!')
        sleep(2)
        user_input(scripts)


if __name__ == '__main__':
    main()
