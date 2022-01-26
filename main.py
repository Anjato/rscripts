from scripts import *
from time import sleep


def main():

    RS3_2tDiv.clear()

    scripts = {1: 'RS3_2tDiv', 2: 'Test'}

    for key, value in scripts.items():
        print(key, "=", value)

    try:
        x = int(input())

        if x == 1:
            RS3_2tDiv.main(0, 0)
        elif x == 2:
            RS3_2tDiv.clear()
            print('Test! :)')
            sleep(2)
            main()
        else:
            RS3_2tDiv.clear()
            print("Invalid input, please try again!")
            sleep(2)
            main()

    except ValueError:
        RS3_2tDiv.clear()
        print("Input is not an integer, dumbass!")
        sleep(2)
        main()


main()
