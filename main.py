#!/usr/bin/python
import os, sys
import actions as act
import constants as c
from logger import log as display


def main():
    display("Hello!")
    act.init()
    act.get_out_of_startbox()
    act.go_to_far_side()
    act.go_and_drop_poms()
    act.go_and_dump_blue()
    if c.seeding:
        act.hay_grab()
    act.shutdown()


if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();