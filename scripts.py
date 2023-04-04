import subprocess
import sys
import shared.consts as consts
import iTest.riskManagmentITest as riskManagmentITest
import iTest.emailITest as emailITest
import iTest.sendEmail as sendEmail
import shared.log as log
import shared.functions as functions


def getSysArg(argNumber):
    arg = sys.argv
    if len(arg) > argNumber:
        return arg[argNumber]
    return None


SLEEP_TIME = 3


def scripts():
    arg = getSysArg(1)
    if arg == consts.TEST:
        log.info("Running handlers folder unit tests")
        cmd_str = "python3 -m unittest discover handlers"
        subprocess.run(cmd_str, shell=True)
        functions.sleep(SLEEP_TIME)

        log.info("Running shared folder unit tests")
        cmd_str = "python3 -m unittest discover shared"
        subprocess.run(cmd_str, shell=True)
        functions.sleep(SLEEP_TIME)

        log.info("Running integration tests")
        riskManagmentITest.runTests()
        emailITest.runTests()
        sys.exit()
    if arg == consts.SEND_EMAIL:
        sendEmail.sendEmail()
