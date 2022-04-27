
import time
from typing import * # type: ignore
from ppadb.device import Device
from gui_interaction_automation.android.click_on_image import click_on_image


def open_app_by_icon(
        device      : Device,
        path_images : Union[str, List[str]],
    ) -> bool:
    to_return : bool = False


    # Goes home
    device.shell("input keyevent 3")
    time.sleep(1.0)


    # Slides up opening the app men
    device.shell("input touchscreen swipe 1000 1500 1000 100 ")
    time.sleep(1.0)


    # Goes to the beginning of all the apps
    for i in range(5):
        device.shell("input touchscreen swipe 100  1000 1000 1000")
        time.sleep(0.5)


    # Goes through the pages and finds the app
    for i in range(5):
        clicked = click_on_image(device, path_images)
        if clicked:
            to_return = True
            break
        time.sleep(0.5)
        device.shell("input touchscreen swipe 1000 1000 100  1000")


    return to_return


# import pytesseract
# print(pytesseract.image_to_string(Image.open('test.png')))