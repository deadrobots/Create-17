#!/usr/bin/python
import os, sys
import actions as act
import constants as c


def main():

    print("Hello!")
    act.init()

    act.get_out_of_startbox()
    act.go_to_far_side()
    act.go_and_drop_poms()
    act.go_and_dump_blue()
    act.shutdown()

    if c.seeding:
        act.hay_grab()
    act.shutdown()
    # act.test()
if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();