import pyautogui
from pyautogui import (
    moveRel,
    moveTo,
    scroll,
    size,
    position,
    FailSafeException
)
from time import sleep
from random import randrange


MOVE_TIME = 0.101
CHECK_TIME = 5
MAX_TIME = CHECK_TIME * CHECK_TIME


def center():
    x, y = size()
    moveX, moveY = x / 2, y / 2
    
    try:
        pyautogui.FAILSAFE = False
        moveTo(moveX, moveY)
        pyautogui.FAILSAFE = True
    except Exception as e:
        print(f"Unexpected Error {e}, {type(e)}")


def hiccup():
    lastPosition = position()

    sleep(CHECK_TIME)
    while True:
        try:
            if lastPosition == position():
                if randrange(7) == 1:
                    y = randrange(-1, 1)
                    
                    scroll(y)
                    scroll(-y)
                else:
                    x, y = randrange(-9, 9), randrange(-9, 9)
                    moveRel(x, y, MOVE_TIME)
                    moveEndPos = position()
                    sleep(CHECK_TIME)
                    if moveEndPos == position():
                        moveTo(lastPosition.x, lastPosition.y, MOVE_TIME)
                    else:
                        lastPosition = position()

                sleep(randrange(CHECK_TIME, MAX_TIME))
            else:
                lastPosition = position()
                sleep(CHECK_TIME)
        except KeyboardInterrupt:
            break
        except FailSafeException:
            print("Could not move, moving to center")
            center()
        except Exception as e:
            print(f"Unexpected Error {e}, {type(e)}")
