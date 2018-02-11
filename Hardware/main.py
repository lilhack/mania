from libsoc_zero.GPIO import Button
from time import sleep

btn = Button('GPIO-G')

def setup():
    pass

def loop():
    while True:
        sleep(0.25)
        if btn.is_pressed():
            print('Button is pressed!')
        else:
            print('Button is not pressed!')

if __name__ == '__main__':
    setup()
    loop()
