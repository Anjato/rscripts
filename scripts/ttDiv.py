import threading
import pyautogui
from pynput.keyboard import Listener
import os
from time import sleep
import random
import cursor


running = False
x, y = pyautogui.position()


def main():

    cursor.hide()

    clear()
    print('Press "insert" to start.')
    print('Press "delete" to stop.')
    print('Press "home" to save new coordinates.')
    print('\nX:', x, 'Y:', y, '          ', end='\r')

    with Listener(on_press=on_press) as listener:
        listener.join()


def on_press(key):
    global running
    global x, y

    if "{}".format(key) == "Key.insert":
        if not running:
            running = True
            threading.Thread(target=process).start()

    elif "{}".format(key) == "Key.home":
        if not running:
            x, y = pyautogui.position()
            print('\rX:', x, 'Y:', y, '          ', end='\r')
        if running:
            pass

    elif "{}".format(key) == "Key.delete":
        if running:
            running = False


def process():
    clear()
    print('Press "delete" to stop.')
    print('\nX:', x, 'Y:', y, '          ', end='\r')

    while running:
        pyautogui.click(x + random.randint(0, 20), y + random.randint(5, 20))
        sleep(1 + random.gauss(0.1, 0.1))

    clear()
    print('Press "insert" to start.')
    print('\nX:', x, 'Y:', y, '          ', end='\r')


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
