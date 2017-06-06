from movement import *
from utils import *
import constants as c
from wallaby import *


def init():
    create_disconnect()
    if not create_connect_once():
        print "Create not connected..."
        exit(0)
    create_full()
    if c.IS_CLONE:
        print "I AM CLONE"
    elif c.IS_PRIME:
        print "I AM PRIME"
    else:
        print "I DON'T KNOW WHAT I AM"
    set_servo_position(c.SERVO_ARM, c.ARM_DOWN)
    set_servo_position(c.SERVO_CLAW, c.CLAW_OPEN)
    set_servo_position(c.SERVO_HAY_ARM, c.HAY_ARM_UP)
    enable_servos()
    msleep(500)
    startup_test()
    wait_for_button(True)
    move_servo(c.SERVO_ARM, c.ARM_UP)
    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_DRIVE)
    infinite_y()
    print"Press the left button to run seeding code and right to run head to head code"
    while not left_button() or right_button():
        pass
    if left_button():
        c.seeding = True
        print "seeding"
    elif right_button():
        c.seeding = False
        print "head to head"
    c.START_TIME = seconds()

def shutdown():
    create_safe()
    create_disconnect()
    print "DONE"
    EXIT()


def startup_test():
    if on_black():
        print "Start the robot on white!"
        exit(0)
    print "Bump right"
    while right_bumped():
        pass
    while not right_bumped():
        pass
    while right_bumped():
        pass
    print "Right Bumped"
    print "Bump left"
    while left_bumped():
        pass
    while not left_bumped():
        pass
    while left_bumped():
        pass
    print "Left Bumped"
    drive_conditional(100, 100, on_black, False)
    move_servo(c.SERVO_ARM, c.ARM_UP)
    move_servo(c.SERVO_CLAW, c.CLAW_OPEN, 100)
    msleep(500)
    move_servo(c.SERVO_CLAW, c.CLAW_CLOSE, 100)
    move_servo(c.SERVO_CLAW, c.CLAW_OPEN, 100)
    move_servo(c.SERVO_ARM, c.ARM_DOWN)
    y()
    y_not()


def test():
    create_disconnect()
    if not create_connect_once():
        print "Create not connected..."
        exit(0)
    create_drive_direct(-500, -500)
    msleep(5000)
###################################################


def get_out_of_startbox():
    # move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_UP)
    move_servo(c.SERVO_ARM, c.ARM_DOWN)
    drive_forever(200, 200)
    while not on_black_right() and not on_black_left():
        pass
    if on_black_left():
        drive_forever(0, 200)
        while not on_black_right():
            pass
    elif on_black_right():
        drive_forever(200, 0)
        while not on_black_left():
            pass
    stop()
    move_servo(c.SERVO_CLAW, c.CLAW_CLOSE, 100)
    msleep(100)
    move_servo(c.SERVO_ARM, c.ARM_UP, 100)
    drive_timed(200, 200, 650)
    if c.IS_PRIME:
        rotate(-100, 1500)
    else:
        rotate(-100, 1615)
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
    # msleep(1000)

    while not approach_furrow():
        drive_timed(-100, -100, 1000)
    stop()

    move_servo(c.SERVO_ARM, c.ARM_DROP, 40)
    msleep(500)
    move_servo(c.SERVO_CLAW, c.CLAW_OPEN, 250)
    msleep(500)
    move_servo(c.SERVO_ARM, c.ARM_UP, 35)
    msleep(100)
    # move_servo(c.SERVO_CLAW, c.CLAW_CLOSE, 250)
    # msleep(300)
    # move_servo(c.SERVO_ARM, c.ARM_DROP, 35)
    # msleep(300)
    # move_servo(c.SERVO_ARM, c.ARM_UP, 35)


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
        rotate(-90, 1800)
    else:
        drive_timed(500, 500, 30)
        rotate(-90, 1700)
    drive_timed(300, 300, 1700)

    if c.IS_PRIME:
        drive_timed(-320, -360, 300)
        rotate(-90, 650)
    else:
        drive_timed(-320, -360, 450)
        rotate(-90, 460)
    drive_timed(-200, -200, 2750)  # was 2500
    move_servo(c.SERVO_ARM, c.ARM_DROP)
    y()
    drive_timed(-250, -250, 300)
    wait_for_button()
    drive_forever(-200, -200)
    while not bumped():
        pass
    stop()



def hay_grab():
    drive_timed(200, 200, 1500)
    y_not()
    drive_forever(100, 100)
    while not on_black_right() and not on_black_left():
        pass
    if on_black_left():
        drive_forever(0, 200)
        while not on_black_right():
            pass
    elif on_black_right():
        drive_forever(200, 0)
        while not on_black_left():
            pass
    stop()
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_STORE)
    drive_timed(250, 250, 1500)
    move_servo(c.SERVO_ARM, c.ARM_DROP)
    #Rotates to angle towards hay
    rotate(-100, 500)
    #Drives to hay and rotates to be parallel to the wall
    drive_timed( -200, -200, 3250)
    rotate(100,2000)
    #Backs up to leave room for hay arm
    #This value may need to be fixed
    drive_timed(100,100,800)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_GATHER)
    #Collects hay
    #Distance has not been checked yet
    drive_forever(-250, -250)
    while not on_black():
        pass
    stop()
    drive_timed(-150, -150, 300)
    #Goal of this code is to line up with hay and pick up all three
    hay_arm(-50)

