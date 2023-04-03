import iTest.riskManagmentITest as riskManagmentITest
import iTest.emailITest as emailITest
import iTest.sendEmail as sendEmail
import iTest.heplers as heplers
import sys


def runIntegrationTests():
    if heplers.isTest():
        riskManagmentITest.runTests()
        emailITest.runTests()
        sys.exit()
    if heplers.isSendEmail():
        sendEmail.sendEmail()
