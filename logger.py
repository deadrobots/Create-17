import logging
from time import strftime
import constants as c
from wallaby import seconds
import os
import subprocess


def log(message):
    print(message)
    datetime = strftime("%Y-%m-%d %H:%M:%S")
    if c.LOGFILE == "":
        name = "{} {}".format(c.ROBOT_NAME, datetime)
        path = "/home/root/Documents"
        os.system("mkdir -p '{}'/logs".format(path))
        os.system("mkdir -p '{}'/logs/{}".format(path, c.ROBOT_NAME))
        c.LOGFILE = "{}/logs/{}/{}".format(path, c.ROBOT_NAME, name)
        open(c.LOGFILE, "w").close()
    dt = "{:.3f}".format(seconds() - c.START_TIME)
    FORMAT = '%(datetime)s %(dt)s: %(message)s'
    logging.basicConfig(filename=c.LOGFILE, format=FORMAT)
    data = {'dt': dt, 'datetime': datetime}
    # print(str(data) + " " + message)
    logging.warning(message, extra=data)


def data_log(message, filename="general.log"):
    dt = seconds() - c.START_TIME
    FORMAT = '%(dt)s\t%(message)s'
    logging.basicConfig(filename=filename, format=FORMAT)
    data = {'dt': dt}
    # print(str(data) + " " + message)
    logging.warning(message, extra=data)