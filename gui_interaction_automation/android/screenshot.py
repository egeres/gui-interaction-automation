
from ppadb.device import Device
def screenshot(device:Device, filename:str) -> None:
    """Takes a screenshot of the device"""

    result = device.screencap()
    with open(filename, "wb") as fp:
        fp.write(result)



if __name__ == "__main__":

    import numpy as np
    import PIL.Image as Image
    import matplotlib
    import matplotlib.pyplot as plt
    from typing import * # type: ignore
    from gui_interaction_automation.android import connect_android

    with connect_android("RFCMB00509J") as device:

        c = 0
        while True:

            screenshot(device, rf"C:\Users\Cherrypie\Desktop\ugh_{c}.png")

            result = device.screencap()
            with open("tmpfile.png", "wb") as fp:
                fp.write(result)
            img    = Image.open("tmpfile.png")
            img_np = np.array(img)
            if img_np.shape[-1] == 4:
                img_np = img_np[:,:,:3]

            plt.imshow(img_np)
            plt.show()

            c += 1

            p = 0