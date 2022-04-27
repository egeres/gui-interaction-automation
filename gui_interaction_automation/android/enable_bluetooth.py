
import time
from ppadb.device import Device
from gui_interaction_automation.android.click_on_image import click_on_image

def enable_bluetooth(device:Device):

    # Open the menu
    device.shell("am start -a android.settings.BLUETOOTH_SETTINGS")
    time.sleep(5.0)


    # Click on the bluetooth if it's off
    clicked = click_on_image(
        device,
        "images/button_bluetooth_off.png",
        debug = True,
    )


