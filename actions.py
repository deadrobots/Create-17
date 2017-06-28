from movement import *
from utils import *
import constants as c
from wallaby import *
from logger import log as display


def init():
    create_disconnect()
    if not create_connect_once():
        display("Create not connected...")
        exit(0)
    create_full()
    if c.IS_CLONE:
        display ("I AM CLONE")
    elif c.IS_PRIME:
        display ("I AM PRIME")
    else:
        display ("I DON'T KNOW WHAT I AM")
    set_servo_position(c.SERVO_ARM, c.ARM_DOWN)
    set_servo_position(c.SERVO_CLAW, c.CLAW_OPEN)
    set_servo_position(c.SERVO_HAY_ARM, c.HAY_ARM_BARN)
    set_servo_position(c.SERVO_HAY_SPIN, c.HAY_SPIN_DRIVE)
    enable_servos()
    msleep(500)
    startup_test()

    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_BARN)
    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_DRIVE)

    move_servo(c.SERVO_ARM, c.ARM_BACK)
    #These servo movements allow the create to fit inside the start box
    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_START)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_START)
    infinite_y()
    display("Press the left button to run seeding code and right to run head to head code")
    while not left_button() or right_button():
        pass
    if left_button():
        c.seeding = True
        display("seeding")
    elif right_button():
        c.seeding = False
        display("head to head")
    while left_button() or right_button():
        pass
    #wait_4_light()
    msleep(500)
    wait_for_button(True)
    c.START_TIME = seconds()


def shutdown():
    create_safe()
    create_disconnect()
    display ("DONE")
    EXIT()


def startup_test():
    if on_black():
        display ("Start the robot on white!")
        exit(0)
    display ("Bump right")
    while right_bumped():
        pass
    while not right_bumped():
        pass
    while right_bumped():
        pass
    display ("Right Bumped")
    display ("Bump left")
    while left_bumped():
        pass
    while not left_bumped():
        pass
    while left_bumped():
        pass
    display ("Left Bumped")
    y()
    y_not()
    # print "push the button"
    wait_for_button(True)
    drive_conditional(100, 100, on_black_and, False)
    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_DRIVE)
    move_servo(c.SERVO_ARM, c.ARM_UP)
    move_servo(c.SERVO_CLAW, c.CLAW_OPEN, 100)
    msleep(500)
    rotate_until_stalled(-50, c.HAY_MOTOR)
    move_servo(c.SERVO_CLAW, c.CLAW_CLOSE, 100)
    move_servo(c.SERVO_CLAW, c.CLAW_OPEN, 100)
    move_servo(c.SERVO_ARM, c.ARM_DOWN)
    wait_for_someone_to_rotate(c.HAY_MOTOR)
    drive_timed(-100, -100, 800)
    display ("Place poms and hay")
    wait_for_button(True)
    rotate_until_stalled(-20, c.HAY_MOTOR)



def test():
    create_disconnect()
    if not create_connect_once():
        display ("Create not connected...")
        exit(0)
    create_drive_direct(-500, -500)
    msleep(5000)


###################################################


def get_out_of_startbox():

    if c.IS_PRIME:
        move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_UP)
    else:
        move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_START_BOX)
    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_DRIVE)
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
        drive_timed(100, 100, 200)
        # rotate(-100, 1400)
        rotate_degrees(-80, 100)
    else:
        rotate(-100, 1500)


def go_to_far_side():
    if c.IS_PRIME:
        drive_timed(500, 495, 2300)
        # drive_accel(500, 2000)
        # DEBUG()
    else:
        display("Long Drive")
        drive_timed(500, 495, 3000)#2600
    if c.IS_PRIME:
        # rotate(100, 1350)
        drive_timed(0, 300, 1350)
    else:
        # rotate(100, 1350)
        drive_timed(0, 300, 1350)
    drive_timed(200, 195, 1500)
    drive_timed(-400, -390, 400)
    if c.IS_PRIME:
        rotate(-110, 1450)
    else:
        rotate(-110, 1450)
    DEBUG()
    if c.IS_PRIME:
        drive_timed(250, 250, 2000)
    else:
        drive_timed(250, 250, 1750)
    # DEBUG()
    if c.IS_PRIME:
        rotate(95, 1550)
    else:
        rotate(95, 1550)


def go_and_drop_poms():
    while not approach_furrow(100, 5):
        drive_timed(-100, -100, 2000)
        rotate(-100, 250)
    stop()
    while not approach_furrow(50, 5):
        drive_timed(-100, -100, 2000)
        rotate(-100, 250)
    stop()
    move_servo(c.SERVO_ARM, c.ARM_DROP, 40)
    msleep(500)
    move_servo(c.SERVO_CLAW, c.CLAW_OPEN, 250)
    msleep(500)
    move_servo(c.SERVO_ARM, c.ARM_UP, 35)
    msleep(100)


def approach_furrow(speed=100, limit_time=3):
    limit = seconds() + limit_time
    drive_forever(speed, speed)
    while not on_black_left() and not on_black_right() and seconds() < limit:
        pass
    if on_black_right():
        display("on right")
        drive_forever(speed, 0)
        while not on_black_left() and seconds() < limit:
            pass
        drive_forever(0,-speed)
        while on_black_right() and seconds < limit:
            pass
        display("found left")
    elif on_black_left():
        display("on left")
        drive_forever(0, speed)
        while not on_black_right() and seconds() < limit:
            pass
        drive_forever(-speed, 0)
        while on_black_left() and seconds() < limit:
            pass
        display("found right")
    return seconds() < limit


def go_and_dump_blue():
    drive_timed(-400, -400, 1000)
    if c.IS_PRIME:
        rotate(-300,950)#900
    else:
        rotate(-300,900)
    move_servo(c.SERVO_ARM, c.ARM_DROP, 50)
    msleep(2000)#19000
    y()
    # wait_for_button(True)
    msleep(3000)

    end = seconds() + 3
    drive_forever(-200, -200)
    while not bumped() and seconds() < end:
        pass
    if seconds() > end:
        # wait_for_button(True)
        drive_timed(150, 150, 500)
        y_not()
        drive_forever(-200, -200)
        end_two = seconds() + 3
        display("Seconds: {}\t\tend_two: {}\t\tBumped: {}".format(seconds(), end_two, bumped()))
        while not bumped() and seconds() < end_two:
            pass
        display("Seconds: {}\t\tend_two: {}\t\tBumped: {}".format(seconds(), end_two, bumped()))
    stop()


def hay_grab():
    if c.IS_PRIME:
        drive_timed(200, 200, 1700)
    else:
        drive_timed(200, 200, 600)
    y_not()
    drive_forever(-200, -200)
    while not bumped():
        pass
    stop()
    move_servo(c.SERVO_ARM, c.ARM_UP)
    rotate(100, 2400)
    drive_timed(100, 100, 1000)
    drive_timed(-100, -100, 1250)
    # rotate(-100, 1450)
    rotate_degrees(-87, 100)

    drive_forever(100, 100)
    while not on_black_right():
        pass
    stop()
    drive_timed(-100, -100, 800)

    wait_for_button(True)

    # rotate(200, 1500)
    # drive_timed(-200, -200, 300)
    # move_servo(c.SERVO_ARM, c.ARM_UP, 25)
    # rotate(200, 1120)
    # drive_forever(25, 25)
    # # while not on_black_right() and not on_black_left():
    # #     pass
    # # if on_black_left():
    # #     drive_forever(0, 25)
    # #     while not on_black_right():
    # #         pass
    # #     drive_forever(-25, 0)
    # #     while on_black_left() and seconds:
    # #         pass
    # # elif on_black_right():
    # #     drive_forever(25, 0)
    # #     while not on_black_left():
    # #         pass
    # #     drive_forever(0, -25)
    # #     while on_black_right() and seconds:
    # #         pass
    # # stop()
    # # while not on_black_right() and not on_black_left():
    # #     pass
    # # if on_black_left():
    # #     drive_forever(0, 25)
    # #     while not on_black_right():
    # #         pass
    # #     drive_forever(-25, 0)
    # #     while on_black_left() and seconds:
    # #         pass
    # # elif on_black_right():
    # #     drive_forever(25, 0)
    # #     while not on_black_left():
    # #         pass
    # #     drive_forever(0, -25)
    # #     while on_black_right() and seconds:
    # #         pass
    # # stop()
    #
    # while not approach_furrow(100, 10):
    #     drive_timed(-100, -100, 2000)
    #     rotate(-100, 250)
    # stop()
    # while not approach_furrow(25, 15):
    #     drive_timed(-100, -100, 2000)
    #     rotate(-100, 250)
    # stop()
    #
    # if c.IS_PRIME:
    #     drive_timed(-100, -100, 1150)
    #     rotate(-200, 950)
    # else:
    #     drive_timed(-100, -100, 1300)
    #     rotate(-200, 950)
    hay_arm(100, .4)
    # This code is for collecting the hay
    if c.IS_PRIME:
        move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_PICK_DRIVE, 20)
    else:
        move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_PICK_UP, 20)
    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_PICK_UP)
    msleep(500)
    # The hay motor needs to be locked in place for this
    # Positioning may also need to be changed after hardware changes the arm
    if c.IS_PRIME:
        drive_timed(46, 50, 4500)
    else:
        drive_timed(46, 50, 3900)
    # Wait for button so the thin hay arm piece can be put in
    # This code is to grab the hay
    # Hasn't been tested so possibly incorrect approach
    if c.IS_PRIME:
        move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_PICK_UP, 20)
    rotate_until_stalled(-50, c.HAY_MOTOR)
    motor_power(c.HAY_MOTOR,40)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_UP, 20)
    drive_timed(-100,-100,1000)
    rotate(100, 1700) #Rotate to get hay
    # rotate_degrees(85, 100)
    # wait_for_button(True)

    drive_timed(-100,-100,3000)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_BARN, 10)
    rotate(100, 300)
    # drive_t
    # imed(-100,-100,1500)
    drive_forever(-100, -100)
    while not bumped():
        pass
    stop()
    if c.IS_PRIME:
        move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_BARN)
    else:
        move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_BARN)
    # if c.IS_CLONE:
        # rotate(100, 400)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_FLAT)
    freeze(c.HAY_MOTOR)
    msleep(1000)


def rotate_until_stalled(speed, motor):
    counter = 0
    motor_power(motor, -speed)
    previous = abs(get_motor_position_counter(motor))
    start = seconds()
    while counter < 10 and seconds() < start + 5:
        if abs(get_motor_position_counter(motor)) == previous:
            counter += 1
        else:
            counter = 0
            previous = abs(get_motor_position_counter(motor))
        msleep(10)
    freeze(motor)
    if seconds() > start + 5:
        display("Motor was unable to reach stalled position in time.")
    clear_motor_position_counter(motor)


def wait_for_someone_to_rotate(motor):
    display("please spin me back")
    clear_motor_position_counter(motor)
    while abs(get_motor_position_counter(motor)) < 350:
        pass
    display("good job")
