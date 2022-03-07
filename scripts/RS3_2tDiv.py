from threading import Thread, Event
import pyautogui
from pynput.keyboard import Listener
import os
from time import sleep
import random
import cursor
import sys


def main(x, y):

    kill_event = Event()
    flag_event = Event()

    cursor.hide()
    x, y = pyautogui.position()

    clear()
    print('Press "insert" to start.')
    print('Press "delete" to stop.')
    print('Press "escape" to exit.')
    print('Press "home" to save new coordinates.')
    print('\nX:', x, 'Y:', y)

    with Listener(on_press=lambda event: on_press(event, x, y, flag_event, kill_event)) as listener:
        listener.join()


def on_press(key, x, y, flag_event, kill_event):

    if "{}".format(key) == "Key.insert":
        if not flag_event.is_set():
            flag_event.set()
            t = Thread(target=process, args=[x, y, flag_event, kill_event])
            t.daemon = True
            t.start()

    elif "{}".format(key) == "Key.home":
        if not flag_event.is_set():
            x, y = pyautogui.position()
            main(x, y)
        if flag_event.is_set():
            pass

    elif "{}".format(key) == "Key.delete":
        if flag_event.is_set():
            flag_event.clear()

    elif "{}".format(key) == "Key.esc":
        kill_event.set()
        if kill_event.is_set():
            sys.exit(0)


def process(x, y, flag_event, kill_event):

    while flag_event.is_set():
        pyautogui.click(x + random.gauss(0, 3), y + random.gauss(0, 2))
        sleep(1 + random.gauss(0.1, 0.1))
        if kill_event.set():
            sys.exit(0)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
