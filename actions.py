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
    move_servo(c.SERVO_ARM, c.ARM_BACK)
    #These servo movements allow the create to fit inside the start box
    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_START)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_START)
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
    drive_conditional(100, 100, on_black_and, False)
    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_DRIVE)
    move_servo(c.SERVO_ARM, c.ARM_UP)
    move_servo(c.SERVO_CLAW, c.CLAW_OPEN, 100)
    msleep(500)
    move_servo(c.SERVO_CLAW, c.CLAW_CLOSE, 100)
    move_servo(c.SERVO_CLAW, c.CLAW_OPEN, 100)
    move_servo(c.SERVO_ARM, c.ARM_DOWN)
    rotate_until_stalled(-100, c.HAY_MOTOR)
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

    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_DRIVE)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_UP)
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
        rotate(-100, 1400)
    else:
        rotate(-100, 1615)
    wait_for_button()


def go_to_far_side():
    drive_timed(500, 495, 2500)
    rotate(100, 1350)
    drive_timed(300, 295, 1200)
    drive_timed(-400, -390, 390)
    rotate(-110, 1450)
    drive_timed(250, 250, 1900)
    rotate(95, 1550)


def go_and_drop_poms():
    while not approach_furrow():
        drive_timed(-100, -100, 1000)
    stop()

    move_servo(c.SERVO_ARM, c.ARM_DROP, 40)
    msleep(500)
    move_servo(c.SERVO_CLAW, c.CLAW_OPEN, 250)
    msleep(500)
    move_servo(c.SERVO_ARM, c.ARM_UP, 35)
    msleep(100)


def approach_furrow():
    limit = seconds() + 6
    drive_forever(100, 100)
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
    drive_timed(-400, -400, 1000)
    rotate(-300, 900)
    move_servo(c.SERVO_ARM, c.ARM_DROP, 50)
    y()
    drive_forever(-200, -200)
    while not bumped():
        pass
    stop()


def hay_grab():
    drive_timed(200, 200, 1500)
    y_not()
    move_servo(c.SERVO_ARM, c.ARM_UP, 25)
    rotate(200, 1120)
    drive_forever(100, 100)
    while not on_black_right() and not on_black_left():
        pass
    if on_black_left():
        drive_forever(0, 100)
        while not on_black_right():
            pass
    elif on_black_right():
        drive_forever(100, 0)
        while not on_black_left():
            pass
    stop()
    drive_timed(-100, -100, 1500)
    rotate(-200, 850)

    hay_arm(100, .4)
    # This code is for collecting the hay
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_GATHER, 20)
    msleep(500)
    # The hay motor needs to be locked in place for this
    # Positioning may also need to be changed after hardware changes the arm
    drive_timed(46, 50, 4100)
    # Wait for button so the thin hay arm piece can be put in
    # This code is to grab the hay
    # Hasn't been tested so possibly incorrect approach
    rotate_until_stalled(-50, c.HAY_MOTOR)
    motor_power(c.HAY_MOTOR,-40)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_UP, 20)
    drive_timed(-100,-100,1000)
    rotate(100, 1500)
    drive_timed(-100,-100,3000)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_BARN, 10)
    drive_timed(-100,-100,1500)
    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_BARN)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_FLAT)


def rotate_until_stalled(speed, motor):
    counter = 0
    motor_power(motor, speed)
    previous = abs(get_motor_position_counter(motor))
    while counter < 10:
        if abs(get_motor_position_counter(motor)) == previous:
            counter += 1
        else:
            counter = 0
            previous = abs(get_motor_position_counter(motor))
        msleep(10)
    freeze(motor)
    clear_motor_position_counter(motor)

