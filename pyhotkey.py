from pynput import keyboard, mouse

kHotkeys = []
mHotkeys = []

class Hotkey:
    def __init__(self, key, callback, release):
        self.key = key
        self.callback = callback
        self.release = release

    def getActualKey(self, pressedKey):
        pass

    def check(self, pressedKey, release):
        if self.getActualKey(pressedKey) == self.key and self.release == release:
            self.callback()

class KHotkey(Hotkey):
    def getActualKey(self, pressedKey):
        try:
            actualKey = pressedKey.char
        except AttributeError:
            actualKey = pressedKey
        return actualKey

class MHotkey(Hotkey):
    def getActualKey(self, pressedKey):
        return pressedKey

def kHotkey(key, release=False):
    def decorator(func):
        def wrapper():
            kHotkeys.append(KHotkey(key, func, release))
        return wrapper()
    return decorator

def mHotkey(key, release=False):
    def decorator(func):
        def wrapper():
            mHotkeys.append(MHotkey(key, func, release))
        return wrapper()
    return decorator

def onKeyPress(key):
    # print(f'[PRESS] {key}')
    for hotkey in kHotkeys:
        hotkey.check(key, False)

def onKeyRelease(key):
    # print(f'[RELEASE] {key}')
    for hotkey in kHotkeys:
        hotkey.check(key, True)

def onClick(x, y, button, pressed):
    # print(f'[CLICK] {x} {y} {button} {pressed}')
    for hotkey in mHotkeys:
        hotkey.check(button, not pressed)

def runHotkeys():
    mouse.Listener(on_click=onClick).start()

    with keyboard.Listener(on_press=onKeyPress, on_release=onKeyRelease) as keyboardListener:
        keyboardListener.join()