
import os
import cv2
import numpy as np
from typing import * # type: ignore
from ppadb.device import Device
import PIL.Image as Image


def click_on_image(
    device         : Device,
    path_images    : Union[str, List[str]],
    threshold      : float = 0.95,
    debug          : bool  = False,
):
    to_return : bool = False


    result = device.screencap()
    with open("tmpfile.png", "wb") as fp:
        fp.write(result)
    img    = Image.open("tmpfile.png")
    img_np = np.array(img)
    if img_np.shape[-1] == 4:
        img_np = img_np[:,:,:3]


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
            x = pt[0]+int(temp_0_w/2)
            y = pt[1]+int(temp_0_h/2)
            device.shell(f"input tap {x} {y}")
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





