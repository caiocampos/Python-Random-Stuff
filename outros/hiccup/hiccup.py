import pyautogui
from pyautogui import moveRel, moveTo, size, position, FailSafeException
from time import sleep
from random import randrange


CHECK_TIME = 5


def center():
    x, y = size()
    moveX, moveY = x / 2, y / 2
    pyautogui.FAILSAFE = False
    moveTo(moveX, moveY)
    pyautogui.FAILSAFE = True


def hiccup():
    lastPosition = position()

    sleep(CHECK_TIME)
    while True:
        try:
            if lastPosition == position():
                x, y = randrange(-9, 9), randrange(-9, 9)
                moveRel(x, y)
                moveRel(-x, -y)

                sleep(randrange(5, 25))
            else:
                lastPosition = position()
                sleep(CHECK_TIME)
        except KeyboardInterrupt:
            break
        except FailSafeException:
            print("Could not move, moving to center")
            center()


hiccup()
