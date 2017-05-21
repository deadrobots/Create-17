from movement import *
from utils import *
import constants as c


def init():
    set_servo_position(c.SERVO_ARM, c.ARM_DOWN)
    set_servo_position(c.SERVO_CLAW, c.CLAW_OPEN)
    if c.IS_CLONE:
        print "I AM CLONE"
    elif c.IS_PRIME:
        print "I AM PRIME"
    else:
        print "I DON'T KNOW WHAT I AM"
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

    wait_for_button(True)

    drive_forever(200, 200)
    while not on_black_left():
        pass
    stop()
    move_servo(c.SERVO_CLAW, c.CLAW_CLOSE, 100)
    msleep(100)
    move_servo(c.SERVO_ARM, c.ARM_UP, 100)
    drive_timed(200, 200, 650)
    if c.IS_PRIME:
        rotate(-100, 1575)
    else:
        rotate(-100, 1625)

    wait_for_button()


def go_to_far_side():
    split_drive(500, 495, 4000, 3, c.TURN_TIME)  # 15 and 40
    drive_forever(200, 200)
    start = seconds()
    if c.IS_PRIME:
        add = 3
    else:
        add = 2
    while seconds() < start + add and not dropped():
        pass
    stop()
    msleep(600)


def go_and_drop_poms():
    if c.IS_PRIME:
        drive_timed(-300, -300, 700)  # 700 900 1100
        rotate(300, 600)  # 650
    else:
        drive_timed(-300, -300, 1100)
        rotate(300, 650)

    wait_for_button()

    drive_timed(100, 100, 750)
    msleep(1000)

    while not approach_furrow():
        drive_timed(-100, -100, 1000)
    stop()

    set_servo_position(c.SERVO_ARM, c.ARM_DROP)
    msleep(500)
    set_servo_position(c.SERVO_CLAW, c.CLAW_OPEN)
    msleep(500)
    set_servo_position(c.SERVO_ARM, c.ARM_UP)
    set_servo_position(c.SERVO_CLAW, c.CLAW_CLOSE)
    msleep(300)
    set_servo_position(c.SERVO_ARM, c.ARM_DROP)
    msleep(300)
    set_servo_position(c.SERVO_ARM, c.ARM_UP)


def approach_furrow():
    limit = seconds() + 6
    drive_forever(100, 100)
    # while on_black_left() or on_black_right():
    #     pass
    while not on_black_left() and not on_black_right() and seconds() < limit:
        pass
    if on_black_right():
        print("on right")
        drive_forever(100, 0)
        while not on_black_left() and seconds() < limit:
            pass
        print("found left")
    elif on_black_left():
        print("on left")
        drive_forever(0, 100)
        while not on_black_right() and seconds() < limit:
            pass
        print("found right")
    return seconds() < limit


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

    drive_forever(-200, -200)
    while not bumped():
        pass
    if c.IS_PRIME:
        drive_timed(100, 100, 200)
        rotate(-100, 1650)
    else:
        drive_timed(50, 50, 300)
        rotate(-100, 1700)
    drive_timed(150, 150, 3600)
    drive_timed(-80, -120, 2900)

    wait_for_button()

    if c.IS_PRIME:
        rotate(-100, 470)
    else:
        rotate(-100, 470)

    wait_for_button()
    drive_timed(-100, -100, 2000)
    msleep(3000)
    drive_timed(-200, -200, 1970)
    drive_forever(-200, -200)
    while not bumped():
        pass
    stop()
