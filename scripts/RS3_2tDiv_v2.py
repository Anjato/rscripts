from functools import partialmethod
from threading import Thread
import pyautogui
from pynput import keyboard
import os
from time import sleep
import random
import cursor
import sys


class Hotkeys:

    x, y = pyautogui.position()

    def __init__(self):
        self._alive = False

    @property
    def alive(self):
        return self._alive

    def set_state(self, state):
        self._alive = bool(state)

    set_alive = partialmethod(set_state, True)
    set_dead = partialmethod(set_state, False)

    def hotkey_ins(self):
        if not self.alive:
            self.set_alive()
            t = Thread(target=self.process, args=[self.x, self.y])
            t.daemon = True
            t.start()
        else:
            pass

    def hotkey_home(self):
        if not self.alive:
            self.x, self.y = pyautogui.position()
            self.info()
        else:
            pass


    def hotkey_del(self):
        if not self.alive:
            pass
        else:
            self.set_dead()

    def hotkey_esc(self):
        sys.exit(0)

    def process(self, x, y):
        while self.alive:
            pyautogui.click(x + random.gauss(0, 3), y + random.gauss(0, 2))
            sleep(1 + random.gauss(0.1, 0.1))
            if not self.alive:
                break

    def info(self):
        if not self.alive:
            cursor.hide()

            clear()
            print('Press "insert" to start.')
            print('Press "delete" to stop.')
            print('Press "escape" to exit.')
            print('Press "home" to save new coordinates.')
            print('\nX:', self.x, 'Y:', self.y)
        else:
            pass


def main(*args):

    h = Hotkeys()
    h.info()

    with keyboard.GlobalHotKeys({
        '<45>': h.hotkey_ins,
        '<36>': h.hotkey_home,
        '<46>': h.hotkey_del,
        '<27>': h.hotkey_esc,
    }) as h: h.join()


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


if __name__ == '__main__':
    print('ERROR: Cannot run module directly. Please run the main loader.')
    os.system('pause' if os.name == 'nt' else 'read -s -n 1 -p "Press any key to continue..."')