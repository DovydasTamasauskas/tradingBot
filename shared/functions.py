

import time
import json
import shared.consts as consts
import shared.print as log


def slice(val: str, start=0, end=None):
    return val[start:end]


def sleep(sleepTime):
    for x in range(sleepTime):
        time.sleep(1)
        print(sleepTime-x, end="\r")


def toJson(subject):
    try:
        return json.loads(slice(subject, len(consts.BOT)))
    except:
        log.error(consts.FAILED_TO_READ_PROPS)