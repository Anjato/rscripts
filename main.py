from scripts import *
from time import sleep


def main():

    ttDiv.clear()

    scripts = {1: '2tDiv', 2: 'Test'}

    for key, value in scripts.items():
        print(key, "=", value)

    try:

        x = int(input())

        if x == 1:
            ttDiv.main()
        elif x == 2:
            ttDiv.clear()
            print('Test! :)')
            sleep(2)
            main()
        else:
            ttDiv.clear()
            print("Invalid input, please try again!")
            sleep(2)
            main()

    except ValueError:
        ttDiv.clear()
        print("Input is not an integer, dumbass!")
        sleep(2)
        main()


main()
