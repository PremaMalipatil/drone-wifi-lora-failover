import serial
from config.settings import LORA_PORT, LORA_BAUDRATE

class LoRaSender:
    def __init__(self):
        self.ser = serial.Serial(LORA_PORT, LORA_BAUDRATE, timeout=1)

    def send(self, message):
        self.ser.write((message + "\n").encode())
        print(f"LoRa Sent: {message}")
