
import pyautogui
from termcolor import colored

pyautogui.FAILSAFE = False # Why was this needed...?

def typetext(text:str, debug:bool=True):
    if debug:
        print("\t", colored("-", "yellow"), text)
    pyautogui.typewrite(text)

