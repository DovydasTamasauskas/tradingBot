

import time
import json
import shared.consts as consts
import shared.log as log


def slice(val: str, start=0, end=None):
    return val[start:end]


def sleep(sleepTime):
    for x in range(sleepTime):
        time.sleep(1)
        print(sleepTime-x, end="\r")


def toJson(subject):
    try:
        return json.loads(subject)
    except Exception as inst:
        print(inst)
        log.warrning(consts.FAILED_TO_READ_PROPS)
        return None


def decode(value):
    try:
        return value.decode('utf8').replace("'", '"')
    except:
        log.warrning(consts.FAILED_TO_DECODE_EMAIL_MESSAGE)


def isResultMessage(subject):
    prefix = consts.RESULTS
    return subject[0:len(prefix)] == prefix
