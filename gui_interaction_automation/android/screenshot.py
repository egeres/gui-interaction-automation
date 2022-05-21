
from ppadb.device import Device
def screenshot(device:Device, filename:str) -> None:
    """Takes a screenshot of the device"""

    result = device.screencap()
    with open(filename, "wb") as fp:
        fp.write(result)


if __name__ == "__main__":

    from gui_interaction_automation.android import connect_android

    with connect_android("RFCMB00509J") as device:
        while True:
            screenshot(device, r"C:\Users\Cherrypie\Desktop\s.png")
            p = 0