import time
from wifi.wifi_monitor import wifi_connected
from wifi.rsync_transfer import start_rsync
from lora.lora_sender import LoRaSender
from config.settings import WIFI_CHECK_INTERVAL

class FailoverManager:

    def __init__(self):
        self.lora = LoRaSender()
        self.wifi_status = True

    def run(self):
        while True:
            if wifi_connected():
                if not self.wifi_status:
                    print("WiFi Restored!")
                    self.lora.send("WIFI_RESTORED")
                    self.wifi_status = True

                print("WiFi Active → Using rsync")
                start_rsync()

            else:
                if self.wifi_status:
                    print("WiFi Lost! Switching to LoRa")
                    self.lora.send("WIFI_LOST")
                    self.wifi_status = False

                print("Using LoRa Backup Mode")
                self.lora.send("STATUS: LOW_BANDWIDTH_MODE")

            time.sleep(WIFI_CHECK_INTERVAL)
