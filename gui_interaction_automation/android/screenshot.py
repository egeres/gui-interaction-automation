
from ppadb.device import Device

def screenshot(device:Device, filename:str) -> None:
    """Takes a screenshot of the device"""

    result = device.screencap()
    with open(filename, "wb") as fp:
        fp.write(result)
