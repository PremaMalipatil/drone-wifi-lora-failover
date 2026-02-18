import os
from config.settings import GROUND_IP, PING_COUNT

def wifi_connected():
    response = os.system(f"ping -c {PING_COUNT} {GROUND_IP} > /dev/null 2>&1")
    return response == 0
