import threading
import pyautogui
from pynput.keyboard import Listener
import os
from time import sleep
import random
import cursor


running = False


def main(x, y):
    cursor.hide()
    x, y = pyautogui.position()

    clear()
    print('Press "insert" to start.')
    print('Press "delete" to stop.')
    print('Press "home" to save new coordinates.')
    print('\nX:', x, 'Y:', y)

    with Listener(on_press=lambda event: on_press(event, x, y)) as listener:
        listener.join()


def on_press(key, x, y):
    global running

    if "{}".format(key) == "Key.insert":
        if not running:
            running = True
            t = threading.Thread(target=process, args=[x, y])
            t.daemon = True
            t.start()

    elif "{}".format(key) == "Key.home":
        if not running:
            x, y = pyautogui.position()
            main(x, y)
        if running:
            pass

    elif "{}".format(key) == "Key.delete":
        if running:
            running = False


def process(x, y):

    while running:
        pyautogui.click(x + random.gauss(0, 3), y + random.gauss(0, 2))
        sleep(1 + random.gauss(0.1, 0.1))


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
