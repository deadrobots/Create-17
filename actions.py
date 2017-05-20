from movement import *
from utils import *
import constants as c

def init():
    c.START_TIME = seconds()
    enable_servos()
    create_disconnect()
    if not create_connect_once():
        print "Create not connected..."
        exit(0)
    create_full()


def shutdown():
    create_safe()
    create_disconnect()
    print "DONE"
    EXIT()


###################################################


def get_out_of_startbox():
    drive_forever(100, 100)
    while not on_black_left():
        pass
    stop()
    drive_timed(100, 100, 1300)
    rotate(-100, 1625)

    wait_for_button()


def go_to_far_side():
    split_drive(500, 495, 4000, 3, c.TURN_TIME)  # 15 and 40
    drive_timed(500, 500, 1000)
    drive_timed(100, 100, 1000)
    msleep(600)


def go_and_dump():
    drive_timed(-300, -300, 900)  # 700 900 1100
    rotate(300, 600)  # 650

    wait_for_button()

    drive_forever(100, 100)
    while on_black_left() or on_black_right():
        pass
    while not on_black_left() and not on_black_right():
        pass
    if on_black_right():
        drive_forever(100, 0)
        while not on_black_left():
            pass
    elif on_black_left():
        drive_forever(0, 100)
        while not on_black_right():
            pass
    stop()

    msleep(3000)


def go_and_dump_blue():
    drive_timed(-200, -200, 2500)  # 3000

    wait_for_button()

    drive_forever(-100, -100)
    while not on_black_right() and not on_black_left():
        pass
    if on_black_left():
        drive_forever(0, -200)
        while not on_black_right():
            pass
    elif on_black_right():
        drive_forever(-200, 0)
        while not on_black_left():
            pass
    stop()

    wait_for_button()

    rotate(-200, 1350)  # 1400

    msleep(2000)
    wait_for_button()

    drive_timed(-200, -200, 2000)
    drive_forever(-200, -200)
    while not bumped():
        pass
    stop()
