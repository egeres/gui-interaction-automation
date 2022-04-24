
import subprocess
from ppadb.client import Client as AdbClient
from ppadb.device import Device

class connect_android():

    def __init__(self, device_id:str):
        out = subprocess.check_output(["adb", "devices"], shell=True).decode()
        if not device_id in out:
            ValueError("Device is not listed")
        self.device_id : str = device_id

    def __enter__(self) -> Device: 
        self.client    : AdbClient = AdbClient(host="127.0.0.1", port=5037)
        device         : Device    = self.client.device(self.device_id)
        return device

    def __exit__(self, type, value, traceback):
        self.client.remote_disconnect()
