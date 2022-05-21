
from typing import *
import os
import cv2
import numpy as np
from PIL import ImageGrab
from PIL import Image
import win32api
import win32con
from time import sleep

# 💊 Point and click nuevo!
def point_and_click(
        path_images    : Union[List[str], str],
        threshold      : float           = 0.95,
        offset_click   : Tuple[int, int] = (0,0),
        mandatory      : bool            = False, # If enabled, when no click is founds it creates a report of bugs and exits the code
        clicks         : int             = 1,
        pre_move_to_00 : bool            = True,
        descr          : str             = "",
    ) -> bool:

    # Mmm
    offset_monitor = (0, 0)

    # 💊 Optional pre-move of the cursor before a click happens
    # This ensures that no overlay-css is causing issues with the image recognition system
    if pre_move_to_00:
        sleep(1.0)
        win32api.SetCursorPos((0, 0))
        sleep(1.0)

    # 💊 Assert value type + small change
    if isinstance(path_images, str):
        path_images = [path_images]
    elif all([isinstance(x, str) for x in path_images]):
        pass
    else:
        raise ValueError("Woopsie, path_images is not a string or list of strings")

    # WIP, el screensize se combina directamente y me da palo fixearlo, de momento haré esto a mano
    # img    = ImageGrab.grab(bbox=(0,0+offset_monitor[1],1920*3,1080), all_screens=True)
    img    = ImageGrab.grab(bbox=(0+offset_monitor[0],0+offset_monitor[1],1920*2,1080), all_screens=True)
    img_np = np.array(img)

    to_return : bool = False

    for sub_path_image in path_images:
        
        if not os.path.exists(sub_path_image):
            raise ValueError("Hey bro! The image '" + sub_path_image + "' doesn't exist")

        spr                = cv2.cvtColor(cv2.imread(sub_path_image), cv2.COLOR_BGR2RGB)
        temp_0_w, temp_0_h = spr.shape[1], spr.shape[0]
        res = cv2.matchTemplate(img_np, spr, cv2.TM_CCOEFF_NORMED)
        loc = np.where(res >= threshold)
        count = 0
        for pt in zip(*loc[::-1]):
            count += 1
        # print (count)
        # print (loc)
        if count >= 1 and count <= 20:
            x = pt[0]+int(temp_0_w/2) + offset_monitor[0] + offset_click[0]
            y = pt[1]+int(temp_0_h/2) + offset_monitor[1] + offset_click[1]
            # print (x, y)

            print (
                "\t",
                colored("*", "yellow"),
                "Clicking...",
                sub_path_image.ljust(60),
                "("+str(x).ljust(4)+","+str(y).ljust(4)+")",
                descr,
            )

            win32api.SetCursorPos((x,y))
            for i in range(clicks):
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,x,y,0,0)
                win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,  x,y,0,0)
                sleep(0.1)

            to_return = True

            break
    
    if mandatory and not to_return:
        a = "debug_" + str(random.randint(0, 100000)) + ".png"
        print (colored("Error", "red"), ": I didn't find ", path_images)
        print ("Closing this but making a debug image '"+a+"'")
        img2 = Image.fromarray(img_np, "RGB")
        img2.save(a)
        p=0
        exit(0)

    return to_return


    