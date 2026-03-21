from evdev import UInput, InputDevice, list_devices, ecodes
from time import sleep
from random import randrange
from math import copysign
from select import select

MOVE_TIME = 0.071
CHECK_TIME = 5
MAX_TIME = CHECK_TIME * CHECK_TIME

capabilities = {ecodes.EV_REL: (ecodes.REL_X, ecodes.REL_Y, ecodes.REL_WHEEL)}

uInput = UInput(capabilities, name="virtual-pointer-hiccup")


def smooth_move(dx: int, dy: int, duration: int, steps: int = 10):
    if steps <= 0:
        return

    sleepTime = duration / steps
    stepX = dx / steps
    stepY = dy / steps
    accStepX = 0.0
    accStepY = 0.0

    for _ in range(steps):
        accStepX += stepX
        accStepY += stepY
        intStepX = int(accStepX)
        intStepY = int(accStepY)
        accStepX -= intStepX
        accStepY -= intStepY
        uInput.write(ecodes.EV_REL, ecodes.REL_X, intStepX)
        uInput.write(ecodes.EV_REL, ecodes.REL_Y, intStepY)
        uInput.syn()

        sleep(sleepTime)


def smooth_scroll(dy: int, duration: int):
    if dy == 0:
        return

    sleepTime = duration / abs(dy)

    for _ in range(abs(dy)):
        uInput.write(ecodes.EV_REL, ecodes.REL_WHEEL, int(copysign(1, dy)))
        uInput.syn()

        sleep(sleepTime)


def find_mouses() -> list[InputDevice[str]] | None:
    devices: list[InputDevice[str]] = []
    for path in list_devices():
        dev = InputDevice(path)
        name = dev.name.lower()
        if "mouse" in name or "touchpad" in name:
            devices.append(dev)
        
    if len(devices) > 0:
        return devices
    
    return None


def has_moved(devices: list[InputDevice[str]], timeout: int) -> bool:
    r, _, _ = select(devices, [], [], timeout)
    if r:
        for device in devices:
            for event in device.read():
                if event.type == ecodes.EV_REL:
                    return True
    return False


def hiccup():
    mouses = find_mouses()

    sleep(CHECK_TIME)
    while True:
        try:
            hasMoved = has_moved(mouses, CHECK_TIME)
            if not hasMoved:
                if randrange(17) == 1:
                    y = randrange(-1, 1)

                    smooth_scroll(y, MOVE_TIME)
                    smooth_scroll(-y, MOVE_TIME)
                else:
                    x, y = randrange(-9, 9), randrange(-9, 9)
                    smooth_move(x, y, MOVE_TIME)
                    sleep(CHECK_TIME)
                    hasMoved = has_moved(mouses, CHECK_TIME)
                    if not hasMoved:
                        smooth_move(-x, -y, MOVE_TIME)

                sleep(randrange(CHECK_TIME, MAX_TIME))
            else:
                sleep(CHECK_TIME)
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Unexpected Error {e}, {type(e)}")
