#!/usr/bin/python
import urllib
from time import sleep
from gpio_96boards import GPIO

filename = "myphone.txt"
url = "http://127.0.0.1:5000/api/messagecontacts?myphone="
GPIO_A = GPIO.gpio_id('GPIO_A')
pins = (
    (GPIO_A, 'in'),
)

def setup(filename):
    with open(filename) as f:
        phone_no = f.read().strip()
    print(phone_no + "5")
    return phone_no

def loop(gpio, url):
    prev = 0
    while True:
        sleep(0.3)
        curr = gpio.digital_read(GPIO_A)
        if prev == 0 and curr == 1:
            response = urllib.urlopen(url)
            data = response.read()
        prev = curr

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Read Button')
    args = parser.parse_args()

    phone_no = setup(filename)

    with GPIO(pins) as gpio:
        loop(gpio, phone_no)
