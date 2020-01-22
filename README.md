# PyHotkey
A hotkey program  
Written and configured in python
# Installation
```
$ git clone https://github.com/nathansmerrill/pyhotkey ~/pyhotkey
$ pip install ~/pyhotkey/requirements.txt
```
Set `~/pyhotkey/pyhotkeyrc.py` to run on startup
# Configuration
`~/pyhotkey/pyhotkeyrc.py`
## Keyboard hotkey
```python
@pyhotkey.kHotkey(key, [released])
def handleMyKeyboardHotkey():
    doAction()
```
## Mouse hotkey
```python
@pyhotkey.mHotkey(button, [released])
def handleMyMouseHotkey():
    doAction()
```
## Example
```python
import pyhotkey
from pynput.keyboard import Key
from pynput.mouse import Button

@pyhotkey.kHotkey('a')
def handleA():
    print('A pressed')

@pyhotkey.kHotkey(Key.caps_lock, True)
def handleCapsLockReleased():
    print('Caps lock released')

@pyhotkey.mHotkey(Button.button8)
def handleBackButton():
    print('Mouse back button pressed')

pyhotkey.runHotkeys()
```