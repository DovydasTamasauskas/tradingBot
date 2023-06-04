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


def runCmdProcess(path):
    log.info("Running " + path + " tests")
    cmd_str = "python3 -m unittest " + path
    subprocess.run(cmd_str, shell=True)
    functions.sleep(SLEEP_TIME)


SLEEP_TIME = 1

TEST_PATHS = [
    "shared/test/test_isRequiredParamsDefined.py",
    "shared/test/test_slice.py",
    "handlers/test/test_getTakeProfit.py",
    "handlers/test/test_isStopLossExceeded.py",
    "brokers/interactiveBrokers/test/test_getContract.py",
    "brokers/interactiveBrokers/test/test_handlePosition.py",
    "brokers/interactiveBrokers/test/test_getStopLossHistorical.py",
    "brokers/interactiveBrokers/test/test_getCandles.py"
]


def scripts():
    arg = getSysArg(1)
    if arg == consts.TEST:
        for path in TEST_PATHS:
            runCmdProcess(path)

        log.info("Running integration tests")
        riskManagmentITest.runTests()
        emailITest.runTests()
        sys.exit()
    if arg == consts.SEND_EMAIL:
        sendEmail.sendEmail()
