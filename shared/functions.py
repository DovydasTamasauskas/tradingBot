

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
        return json.loads(slice(subject, len(consts.BOT)))
    except:
        log.error(consts.FAILED_TO_READ_PROPS)


def toJson2(subject):
    try:
        return json.loads(subject)
    except:
        log.error(consts.FAILED_TO_READ_PROPS)


def decodeJson(encodedJson):
    try:
        decodedJson = encodedJson.decode('utf8').replace("'", '"')

        return json.loads(decodedJson)
        # return json.dumps(data, indent=4, sort_keys=True)
    except:
        log.warrning(consts.FAILED_TO_DECODE_JSON)
