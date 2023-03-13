import sys


def slice(val: str, start=0, end=None):
    return val[start:end]


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def log(message):
    print(bcolors.OKGREEN + message + bcolors.ENDC)


def warrning(message):
    print(bcolors.WARNING + message + bcolors.ENDC)


def error(message):
    print(bcolors.FAIL + message + bcolors.ENDC)
    sys.exit()
