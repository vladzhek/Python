import ctypes
import time 
import keyboard
import pyautogui

# C struct redefinitions 
PUL = ctypes.POINTER(ctypes.c_ulong)

class KeyBdInput(ctypes.Structure):
    _fields_ = [("wVk", ctypes.c_ushort),
                ("wScan", ctypes.c_ushort),
                ("dwFlags", ctypes.c_ulong),
                ("time", ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class HardwareInput(ctypes.Structure):
    _fields_ = [("uMsg", ctypes.c_ulong),
                ("wParamL", ctypes.c_short),
                ("wParamH", ctypes.c_ushort)]

class MouseInput(ctypes.Structure):
    _fields_ = [("dx", ctypes.c_long),
                ("dy", ctypes.c_long),
                ("mouseData", ctypes.c_ulong),
                ("dwFlags", ctypes.c_ulong),
                ("time",ctypes.c_ulong),
                ("dwExtraInfo", PUL)]

class Input_I(ctypes.Union):
    _fields_ = [("ki", KeyBdInput),
                 ("mi", MouseInput),
                 ("hi", HardwareInput)]

class Input(ctypes.Structure):
    _fields_ = [("type", ctypes.c_ulong),
                ("ii", Input_I)]

# Actuals Functions

def PressKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

def ReleaseKey(hexKeyCode):
    extra = ctypes.c_ulong(0)
    ii_ = Input_I()
    ii_.ki = KeyBdInput( 0, hexKeyCode, 0x0008 | 0x0002, 0, ctypes.pointer(extra) )
    x = Input( ctypes.c_ulong(1), ii_ )
    ctypes.windll.user32.SendInput(1, ctypes.pointer(x), ctypes.sizeof(x))

#--------------------------------------------------------------------------------------
#---------- START PROGRAM -------------------------------------------------------------
#-------------------------------------------------------------------------------------- 
Start = True

# Hex Key Codes Table FROM  http://www.flint.jp/misc/?q=dik&lang=en
def KeyToHex(Key):
    hexKeyCode = 0
    if(Key == 'Q'): hexKeyCode = 0x10
    elif(Key == 'W'): hexKeyCode = 0x11
    elif(Key == 'E'): hexKeyCode = 0x12
    elif(Key == 'R'): hexKeyCode = 0x13
    elif(Key == 'T'): hexKeyCode = 0x14
    elif(Key == 'Y'): hexKeyCode = 0x15
    elif(Key == 'U'): hexKeyCode = 0x16 
    elif(Key == 'I'): hexKeyCode = 0x17
    elif(Key == 'O'): hexKeyCode = 0x18
    elif(Key == 'P'): hexKeyCode = 0x19
    elif(Key == 'A'): hexKeyCode = 0x1E
    elif(Key == 'S'): hexKeyCode = 0x1F
    elif(Key == 'D'): hexKeyCode = 0x20
    elif(Key == 'F'): hexKeyCode = 0x21
    elif(Key == 'G'): hexKeyCode = 0x22
    elif(Key == 'H'): hexKeyCode = 0x23
    elif(Key == 'J'): hexKeyCode = 0x24
    elif(Key == 'K'): hexKeyCode = 0x25
    elif(Key == 'L'): hexKeyCode = 0x26
    elif(Key == 'Z'): hexKeyCode = 0x2C
    elif(Key == 'X'): hexKeyCode = 0x2D
    elif(Key == 'C'): hexKeyCode = 0x2E
    elif(Key == 'V'): hexKeyCode = 0x2F
    elif(Key == 'B'): hexKeyCode = 0x30
    elif(Key == 'N'): hexKeyCode = 0x31
    elif(Key == 'M'): hexKeyCode = 0x32
    elif(Key == 'Esc'): hexKeyCode = 0x01
    elif(Key == 'Tab'): hexKeyCode = 0x0F  
    elif(Key == 'Alt'): hexKeyCode = 0x38 #Left 
    elif(Key == 'Shift'): hexKeyCode = 0x2A #Left     
    elif(Key == 'Enter'): hexKeyCode = 0x1C
    elif(Key == 'Space'): hexKeyCode = 0x39
    elif(Key == 'CapsLock'): hexKeyCode = 0x3A  
    else: hexKeyCode = Key
    return hexKeyCode

def DownUpKeyTime(KeyOrHex,SleepSecond):
    hexKeyCode = KeyToHex(KeyOrHex)
    PressKey(hexKeyCode)
    time.sleep(SleepSecond)
    ReleaseKey(hexKeyCode) 

def EldenFarm():
    Start = True
    while (Start == True):
        print('Start 2 sec')
        time.sleep(2)
        DownUpKeyTime('A',0.3)
        DownUpKeyTime('W',4)
        DownUpKeyTime('A',0.3)
        DownUpKeyTime('W',1)
    # Shift + MouseButtons
        PressKey(0x2A)
        pyautogui.mouseDown(button='right'); 
        pyautogui.mouseDown(button='left'); 
        pyautogui.mouseUp(button='right')
        pyautogui.mouseUp(button='left'); 
        ReleaseKey(0x2A)
        print('Wait end spell 5 sec')
        time.sleep(5)
        print('Try open MAp')
    # Open Map
        DownUpKeyTime('G',0.15)        
        time.sleep(1) # <--- wait open map
        DownUpKeyTime('S',0.05)
        time.sleep(0.5)
        print('Press E to accept')
        DownUpKeyTime('E',0.05)
        time.sleep(0.5)
        print('Press E to accept')    
        DownUpKeyTime('E',0.05)
        print('Wait loading')    
        time.sleep(5)

print('Press + to Start')
keyboard.add_hotkey('+', EldenFarm)
keyboard.wait('Ctrl + Shift')

