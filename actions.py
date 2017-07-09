from movement import *
from utils import *
import constants as c
from wallaby import *
from logger import log as display


def init():
    display("\nFunction: init\n")
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
    ''' moved to waiting for light
    move_servo(c.SERVO_ARM, c.ARM_BACK)
    #These servo movements allow the create to fit inside the start box
    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_START)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_START)
    infinite_y()
    '''
    # display("Press the left button to run seeding code and right to run head to head code")
    # while not left_button() or right_button():
    #     pass
    # if left_button():
    #     c.seeding = True
    #     display("seeding")
    # elif right_button():
    #     c.seeding = False
    #     display("head to head")
    wait_4_light()
    shut_down_in(119)
    c.START_TIME = seconds()


def shutdown():
    display("\nFunction: shutdown\n")
    create_safe()
    create_disconnect()
    display ("DONE")
    EXIT()


def startup_test():
    display("\nstartup_test\n")
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
    display("\ntest\n")
    create_disconnect()
    if not create_connect_once():
        display ("Create not connected...")
        exit(0)
    create_drive_direct(-500, -500)
    msleep(5000)


###################################################


def get_out_of_startbox():
    display("\nFunction: get_out_of_startbox\n")
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
        rotate_degrees(-85, 100)
    else:
        drive_timed(100, 100, 200)
        rotate_degrees(-76, 100)


def go_to_far_side():
    display("\nFunction: go_to_far_side\n")
    display("Long Drive")
    if c.IS_PRIME:
        drive_timed(500, 495, 2800)
        drive_timed(0, 280, 1400)
    else:
        drive_timed(500, 495, 2600)#3000
        drive_timed(0, 300, 1300)
    drive_timed(200, 195, 1500) #square up
    drive_timed(-100, -100, 1250)
    rotate_degrees(-85, 100)

    end = seconds() + 7
    if c.IS_PRIME:
        drive_forever(75, 85)
    else:
        drive_forever(75, 90)
    while not on_black_right() and seconds() < end:  # or  not front_bumped()
        pass
    if seconds() >= end:  #or front_bumped()
        drive_timed(-96, -100, 500)
    stop()
    drive_timed(-100, -100, 800)

    if c.IS_PRIME:
        rotate(110, 1450)
    else:
        rotate(110, 1550)


def go_and_drop_poms():
    display("\nFunction: go_and_drop_poms\n")
    while not approach_furrow2(100, 4):
        drive_timed(-100, -100, 2000)
        rotate(-100, 250)
    stop()
    while not approach_furrow2(50, 5):
        drive_timed(-100, -100, 2000)
        rotate(-100, 250)
    stop()
    drive_timed(50,50,400)
    move_servo(c.SERVO_ARM, c.ARM_DROP, 40)
    msleep(500)
    move_servo(c.SERVO_CLAW, c.CLAW_OPEN, 250)
    msleep(500)
    move_servo(c.SERVO_ARM, c.ARM_UP, 35)
    msleep(100)

def approach_furrow(speed=100, limit_time=3):
    display("\nFunction: approach_furrow\n")
    limit = seconds() + limit_time
    drive_forever(speed, speed)
    while not on_black_left() and not on_black_right() and seconds() < limit:
        pass
    if on_black_right():
        drive_forever(speed, 0)
        display("on right")
        while not on_black_left() and seconds() < limit:
            pass
        drive_forever(0,-speed)
        while on_black_right() and seconds < limit:
            pass
        display("found left")
    if on_black_left():
        display("on left")
        drive_forever(0, speed)
        while not on_black_right() and seconds() < limit:
            pass
        drive_forever(-speed, 0)
        while on_black_left() and seconds() < limit:
            pass
        display("found right")
    return seconds() < limit

def approach_furrow2(speed=100, limit_time=3):
    display("\nFunction: approach_furrow\n")
    lspeed = speed
    rspeed = speed
    limit = seconds() + limit_time
    drive_forever(lspeed, rspeed)
    while not on_black_left() and not on_black_right() and seconds() < limit:
        pass
    stop()
    if on_black_left() and on_black_right():
        return seconds() < limit
    if not on_black_right():
        display("not on right")
        drive_forever(0,rspeed)
        while not on_black_right() and seconds() < limit:
            pass
        stop()
        #drive_forever(0,-speed)
        #while on_black_right() and seconds < limit:
        #    pass
        display("aligned right")
    if not on_black_left():
        display("not on left")
        drive_forever(lspeed, 0)
        while not on_black_left() and seconds() < limit:
            pass
        stop()
        #drive_forever(-speed, 0)
        #while on_black_left() and seconds() < limit:
        #    pass
        display("aligned left")
    return seconds() < limit



def go_and_dump_blue():
    display("\nFunction: go_and_dump_blue\n")
    drive_timed(-100, -100, 2500)   #(-400,-400,1000)
    if c.IS_PRIME:
        #rotate(-100,2100)
        rotate_degrees(-123, 100)       #rotation to water tank
    else:
        rotate(-100,2100)
    move_servo(c.SERVO_ARM, c.ARM_DROP, 50)
    msleep(15000)
    if c.IS_CLONE:
        drive_timed(100, 100, 500)
    y()
    # wait_for_button(True)
    msleep(1000)

    end = seconds() + 6
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
    else:
        for _ in range(0, 1):
            stop()
            msleep(2000)
            drive_timed(100, 100, 1200)
            end = seconds() + 6
            drive_forever(-200, -200)
            while not bumped() and seconds() < end:
                pass
        stop()
        msleep(2000)
    stop()


def hay_grab():
    display("\nFunction: hay_grab\n")
    if c.IS_PRIME:
        drive_timed(200, 200, 1700)
    else:
        drive_timed(200, 200, 1700)
    y_not()
    drive_forever(-200, -200)
    while not bumped():
        pass
    stop()
    move_servo(c.SERVO_ARM, c.ARM_UP)
    rotate(100, 2400)
    drive_timed(100, 100, 1000) #square up on pipe

    drive_timed(-100, -100, 1250)
    if c.IS_PRIME:
        rotate_degrees(-89, 100)
    else:
        rotate_degrees(-92, 100)
    end = seconds() + 5
    if c.IS_PRIME:
        drive_forever(75, 95)
    else:
        drive_forever(75, 95)
    while not on_black_right() and seconds() < end: #look for black patch under cow
        pass
    if seconds() >= end: #oops, missed the black patch
        drive_timed(-96,-100,4)
    stop()

    drive_timed(-100, -100, 800)
    if c.IS_PRIME:
        rotate(110, 1450)
    else:
        rotate(110, 1550)
    while not approach_furrow2(100, 5):
        drive_timed(-100, -100, 2000)
        rotate(-100, 250)
    stop()
    while not approach_furrow2(50, 5):
        drive_timed(-100, -100, 2000)
        rotate(-100, 250)
    stop()
    if c.IS_PRIME:
        drive_timed(-100, -100, 1400)
        rotate_degrees(-83, 100)
    else:
        drive_timed(-100, -100, 1300) ###
        rotate_degrees(-86, 100)
    drive_timed(-100, -100, 100)
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
        drive_timed(46, 60, 4600)
    else:
        drive_timed(48, 50, 4800)
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
    #rotate(100, 300)
    # drive_t
    # imed(-100,-100,1500)
    drive_forever(-100, -100)
    while not bumped():
        pass
    stop()
    move_servo(c.SERVO_HAY_SPIN, c.HAY_SPIN_BARN)
    # if c.IS_CLONE:
        # rotate(100, 400)
    move_servo(c.SERVO_HAY_ARM, c.HAY_ARM_FLAT)
    freeze(c.HAY_MOTOR)
    msleep(1000)


def rotate_until_stalled(speed, motor):
    display("\nFunction: rotate_until_stalled\n")
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
    display("\nFunction: wait_for_someone_to_rotate\n")
    display("please spin me back")
    clear_motor_position_counter(motor)
    while abs(get_motor_position_counter(motor)) < 350:
        pass
    display("good job")
