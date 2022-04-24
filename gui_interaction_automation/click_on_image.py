
import os
import cv2
import win32api
import numpy as np
from PIL    import ImageGrab
from PIL    import Image
from time   import sleep
from typing import *

def click_on_image(
    path_images    : Union[List[str], str],
    pre_move_to_00 : bool  = True,
    threshold      : float = 0.95,
    debug          : bool  = False,
    ) -> bool:

    """
    Clicks the given images on the screem

    Args:
        path_images   : Path of strings or string with the image to click.
        pre_move_to_00: If before searching for the image the cursor is moved to the top left coner to avoid highlighting effects.
        threshold     : Threshold to match images, higher makes selection more strict.

    Returns:
        A boolean indicating whether the method actually clicked something.

    """

    to_return      : bool            = False
    offset_monitor : Tuple[int, int] = (0, 0)

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
        raise ValueError("Woopsie, 'path_images' is not a string or list of strings")

    img    = ImageGrab.grab(bbox=(0+offset_monitor[0],0+offset_monitor[1],1920*2,1080), all_screens=True)
    img_np = np.array(img)

    for sub_path_image in path_images:

        if not os.path.exists(sub_path_image):
            raise ValueError(f"Hey! The image '{sub_path_image}' doesn't exist")

        spr                = cv2.cvtColor(cv2.imread(sub_path_image), cv2.COLOR_BGR2RGB)
        temp_0_w, temp_0_h = spr.shape[1], spr.shape[0]
        res                = cv2.matchTemplate(img_np, spr, cv2.TM_CCOEFF_NORMED)
        loc                = np.where(res >= threshold)
        count = 0
        for pt in zip(*loc[::-1]):
            count += 1
        if count >= 1 and count <= 20: # No matches or too many are indicative of a problem
            to_return = True
            break
    
    if debug and not to_return:
        if not os.path.exists("debug"):
            os.makedirs(      "debug")
        amount_of_imgs = len(os.listdir("debug"))
        print (f"\nSaving a debug image as {amount_of_imgs}.png for inputted images...")
        for i in path_images:
            print (f"\t{i}")
        img_pil = Image.fromarray(img_np, "RGB")
        img_pil.save(f"{amount_of_imgs}.png")
            
    return to_return


