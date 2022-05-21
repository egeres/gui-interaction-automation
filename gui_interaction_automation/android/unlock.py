
import time
import numpy as np
import PIL.Image as Image
from ppadb.device import Device

def unlock(device:Device, password:str, debug:bool=False) -> bool:
    """Returns whether the homescreen was unlocked or not. Currently just checks if the screen is very dark to decide if it's blocked"""

    to_return : bool = False

    # Apparently this solves an issue where the image is not fully loaded...
    result = device.screencap()
    with open("tmp.png", "wb") as fp:
        fp.write(result)
    img = Image.open("tmp.png")

    average_color = np.array(img)[:,:,:3].sum(axis=2).mean()
    if (average_color < 50.0):
        device.shell("input keyevent 26")
        device.shell("input touchscreen swipe 1000 2500 1000 100")
        time.sleep(2.0)
        device.shell("input text " + password)
        device.shell("input keyevent 66")
        time.sleep(2.0)
        to_return = True
        if debug: print ("Device was unlocked")
    else:
        if debug: print ("Device wasn't blocked")

    return to_return
