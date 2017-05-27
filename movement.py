from wallaby import *


def drive_timed(left, right, time):
    create_drive_direct(-right, -left)
    msleep(time)
    create_drive_direct(0, 0)


def spin_cw(power, time):
    create_drive_direct(power, -power)
    msleep(time)
    create_drive_direct(0, 0)


def spin_ccw(power, time):
    create_drive_direct(-power, power)
    msleep(time)
    create_drive_direct(0, 0)


def rotate(power, time):
    if power > 0:
        spin_ccw(power, time)
    else:
        spin_cw(abs(power), time)


def split_drive(left, right, time, increments, turnTime):
    power = -100
    if turnTime < 0:
        turnTime = abs(turnTime)
        power = abs(power)
    for _ in range(0, increments):
        drive_timed(left, right, int(time / increments))
        rotate(power, turnTime)


def split_drive_condition(left, right, min, time, turnTime, condition, state=True):
    start = seconds() + time
    create_drive_direct(-left, -right)
    msleep(min)
    while condition() is state:
        current = seconds()
        if current > start:
            start = current + time
            rotate(-100, turnTime)
            create_drive_direct(left, right)
            msleep(min)
    create_drive_direct(0, 0)


def drive_conditional(left, right, testFunction, state=True):
    create_drive_direct(-right, -left)
    while testFunction() is state:
        pass
    stop()


def drive_forever(left, right):
    create_drive_direct(-right, -left)


def stop():
    create_stop()