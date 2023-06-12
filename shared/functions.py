

import time
import json
import shared.consts as consts
import shared.log as log
from datetime import datetime
import shared.functions as functions
import handlers.jsonHandler.setters as setters
import handlers.jsonHandler.getters as getters
import re


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


def isRequiredParamsDefined(json):
    required = ["position", "size", "pair", "time"]
    for param in required:
        try:
            json[param]
        except:
            log.warrning(consts.FAILED_TO_GET_REQUIRED_PARAMS)
            return False
    return True


def getTimeNow():
    return datetime.now().strftime("%H:%M:%S")


def setEnterTimeNow(p):
    timeNow = functions.getTimeNow()
    p = setters.setEnterTime(p, timeNow)
    return p


def getTimeInterval(p):
    time = getters.getTime(p)
    if isinstance(time, int):
        return time
    if time.find("min") != -1:
        return int(re.search(r'\d+', time).group())
    return 15
