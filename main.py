from scripts import *
from time import sleep
import os, glob


def main():

    RS3_2tDiv.clear()

    path = 'scripts/'
    scripts = {}

    i = 1

    try:
        os.chdir(path)
    except EnvironmentError:
        pass

    for file in glob.glob("*.py"):
        if not file == "__init__.py":
            modules = file.replace('.py', '')
            scripts[i] = modules
            i += 1

    for key, value in scripts.items():
        print(key, "=", value)

    try:
        x = int(input())

        if x in scripts:
            eval(scripts[x]+".main()")
        else:
            print("Value does not exist. Try again.")
            sleep(2)

    except ValueError:
        RS3_2tDiv.clear()
        print("Input is not an integer, dumbass!")
        sleep(2)
        main()


main()
