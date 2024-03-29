
import sys

PRINT_WARNINGS = True
PRINT_ERRORS = True


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


def blank(message):
    print(message)


def info(message):
    print(bcolors.OKCYAN + message + bcolors.ENDC)


def success(message):
    print(bcolors.OKGREEN + message + bcolors.ENDC)


def warrning(message):
    if PRINT_WARNINGS == True:
        print(bcolors.WARNING + message + bcolors.ENDC)


def error(message):
    if PRINT_ERRORS == True:
        print(bcolors.FAIL + message + bcolors.ENDC)
        # sys.exit()
