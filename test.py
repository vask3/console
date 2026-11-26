import time
from machine import Pin

# На Pico 2 вграденият LED обикновено е на GP25
led = Pin(25, Pin.OUT)

while True:
    led.toggle()
    time.sleep(0.5)