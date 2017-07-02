from wallaby import digital

# Misc
ALLOW_BUTTON_WAIT = False
START_TIME = 0
CLONE_SWITCH = 9
IS_CLONE = digital(CLONE_SWITCH)
IS_PRIME = not IS_CLONE
STARTLIGHT = 2
FRONT_BUMPED = 0

# Tophats
LEFT_TOPHAT = 0
RIGHT_TOPHAT = 5


THRESHOLD = 1500

# Servos
SERVO_CLAW = 3
SERVO_ARM = 1
SERVO_HAY_SPIN = 2
SERVO_HAY_ARM = 0

#2 1569
#3 170
#1 Same for now
# Motors
Y_ARM = 0
HAY_MOTOR = 1

# Servo Values

if IS_PRIME:
    ARM_OFFSET = -200
    CLAW_OFFSET = 0
    HAY_ARM_OFFSET = 0
    HAY_SPIN_OFFSET = 0
else:
    ARM_OFFSET = -330
    CLAW_OFFSET = 0
    HAY_ARM_OFFSET = 0
    HAY_SPIN_OFFSET = 80

ARM_BACK = 2000#2040
ARM_UP = 1647 + ARM_OFFSET
ARM_DOWN = 380 + ARM_OFFSET
ARM_DROP = 600 + ARM_OFFSET
# if IS_CLONE:
#     ARM_BACK = 1600

CLAW_OPEN = 0 + CLAW_OFFSET
CLAW_CLOSE = 2047 + CLAW_OFFSET

HAY_ARM_FLAT = 1776 + HAY_ARM_OFFSET
HAY_ARM_UP = 500 + HAY_ARM_OFFSET
HAY_ARM_GATHER = 1900 + HAY_ARM_OFFSET
HAY_ARM_STORE = 0 + HAY_ARM_OFFSET
HAY_ARM_BARN = 1200 + HAY_ARM_OFFSET
HAY_ARM_START = 170 + HAY_ARM_OFFSET
HAY_ARM_START_BOX = 620 + HAY_ARM_OFFSET
HAY_ARM_PICK_UP = 1900 + HAY_ARM_OFFSET
HAY_ARM_PICK_DRIVE = 1820 + HAY_ARM_OFFSET
# if IS_CLONE:
#     HAY_ARM_UP = 1270

HAY_SPIN_DRIVE = 1000 + HAY_SPIN_OFFSET
HAY_SPIN_DELIVER = 2040 + HAY_SPIN_OFFSET
HAY_SPIN_BARN = 0
# HAY_SPIN_BARN_CLONE = 250 + HAY_SPIN_OFFSET
HAY_SPIN_START = 1570 + HAY_SPIN_OFFSET
HAY_SPIN_PICK_UP = 800 + HAY_SPIN_OFFSET
# if IS_CLONE:
#     HAY_SPIN_START = HAY_SPIN_DRIVE

# Drive Info
TURN_TIME = 0  # -20  # 0, 15, 40
if IS_CLONE:
    TURN_TIME = 40

seeding = True

LOGFILE = "" # Leave empty
ROBOT_NAME = "Create-17"