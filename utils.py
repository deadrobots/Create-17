'''
Created on Jan 3, 2016
@author: graysonelias
'''

'''
This module provides some of our standard methods.
'''

import constants as c

from wallaby import ao, msleep, digital, seconds, set_servo_position, get_servo_position, right_button, \
    create_drive_direct, create_disconnect, get_create_lbump, get_create_rbump, analog


def wait_for_button():
    if c.ALLOW_BUTTON_WAIT:
        print "Press Button..."
        while not right_button():
            pass
        msleep(1)
        print "Pressed"
        msleep(1000)


def DEBUG(PrintTime=True):
    create_drive_direct(0, 0)
    ao()
    create_disconnect()
    if PrintTime:
        print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    exit(0)


def EXIT():
    create_drive_direct(0, 0)
    ao()
    create_disconnect()
    print 'Program finished!\nSeconds: ', seconds() - c.START_TIME
    exit(0)


def DEBUG_with_wait():
    print 'Program stop for DEBUG\nSeconds: ', seconds() - c.START_TIME
    msleep(5000)
    DEBUG(False)


# Servo Constants
DELAY = 10


# Servo Control #


def move_servo(servo, endPos, speed):  # Moves a servo with increment "speed".
    # speed of 1 is slow
    # speed of 2000 is fast
    # speed of 10 is the default
    now = get_servo_position(servo)
    if speed == 0:
        speed = 2047
    if endPos >= 2048:
        print "Programmer Error"
        exit(0)
    if endPos < 0:
        print "Programmer Error"
        exit(0)
    if now > endPos:
        speed = -speed
    for i in range(int(now), int(endPos), int(speed)):
        set_servo_position(servo, i)
        msleep(DELAY)
    set_servo_position(servo, endPos)
    msleep(DELAY)


def move_servo_timed(servo, endPos, time):  # Moves a servo over a specific time.
    if time == 0:
        speed = 2047
    else:
        speed = abs((DELAY * (get_servo_position(servo) - endPos)) / time)
    move_servo(servo, endPos, speed)


# Loop break timers #

time = 0  # This represents how long to wait before breaking a loop.


def set_wait(DELAY):  # Sets wait time in seconds before breaking a loop.
    global time
    time = seconds() + DELAY


def get_wait():  # Used to break a loop after using "setWait". An example would be: setWiat(10) | while true and getWait(): do something().
    return seconds() < time


def on_black_left():
    return analog(c.LEFT_TOPHAT) > c.THREASHOLD


def on_black_right():
    return analog(c.RIGHT_TOPHAT) > c.THREASHOLD


def bumped():
    return get_create_lbump() or get_create_rbump()