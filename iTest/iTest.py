import iTest.riskManagmentITest as riskManagmentITest
import iTest.emailITest as emailITest
import iTest.heplers as heplers
import sys


def runIntegrationTests():
    if heplers.isTest():
        riskManagmentITest.runTests()
        emailITest.runTests()
        sys.exit()
