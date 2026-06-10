from typing import Iterator
from time import localtime, strftime, sleep
from random import randrange
from math import copysign
from select import select
from evdev import UInput, InputDevice, list_devices
from evdev.ecodes import EV_REL, REL_X, REL_Y, REL_WHEEL
from evdev.events import InputEvent


MOVE_TIME = 0.071
CHECK_TIME = 5
MAX_TIME = CHECK_TIME * CHECK_TIME

capabilities = {EV_REL: (REL_X, REL_Y, REL_WHEEL)}

uInput = UInput(capabilities, name="virtual-pointer-hiccup")


def log(text):
    print(strftime("%H:%M:%S > ", localtime()) + text)


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
        uInput.write(EV_REL, REL_X, intStepX)
        uInput.write(EV_REL, REL_Y, intStepY)
        uInput.syn()

        sleep(sleepTime)


def smooth_scroll(dy: int, duration: int):
    if dy == 0:
        return

    sleepTime = duration / abs(dy)

    for _ in range(abs(dy)):
        uInput.write(EV_REL, REL_WHEEL, int(copysign(1, dy)))
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
            try:
                events: Iterator[InputEvent] = device.read()
                for event in events:
                    if event.type == EV_REL:
                        return True
            except BlockingIOError:
                continue
    return False


def hiccup():
    try:
        log("Starting")
        mouses = find_mouses()

        if mouses is None:
            log("No mouse found!")
            return

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
                    mouses = find_mouses()
                else:
                    sleep(CHECK_TIME)
            except KeyboardInterrupt:
                break
            except OSError as e:
                if e.errno == 19:
                    sleep(CHECK_TIME)
                    mouses = find_mouses()

                log(f"OS Error, {e}, {type(e)}, restarting")
            except Exception as e:
                log(f"Unexpected Error, {e}, {type(e)}, restarting")

    except KeyboardInterrupt:
        return
