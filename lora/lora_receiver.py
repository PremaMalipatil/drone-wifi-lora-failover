import serial
from config.settings import LORA_PORT, LORA_BAUDRATE

class LoRaReceiver:
    def __init__(self):
        self.ser = serial.Serial(LORA_PORT, LORA_BAUDRATE, timeout=1)

    def receive(self):
        if self.ser.in_waiting:
            message = self.ser.readline().decode().strip()
            print(f"LoRa Received: {message}")
            return message
        return None
