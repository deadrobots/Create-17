#!/usr/bin/python
import os, sys
import actions as act


def main():

    print("Hello!")
    act.init()

    act.get_out_of_startbox()
    act.go_to_far_side()
    act.go_and_drop_poms()
    act.go_and_dump_blue()

    act.shutdown()
    # act.test()
if __name__ == "__main__":
    sys.stdout = os.fdopen(sys.stdout.fileno(), "w", 0)
    main();