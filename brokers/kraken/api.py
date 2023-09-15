import time
import json
import base64
import hashlib
import hmac
import urllib.request
import time
import credentials
import handlers.jsonHandler.getters as getters
import shared.log as log
import ssl

api_key_public = credentials.KRAKEN_API_KEY
api_key_private = credentials.KRAKEN_PRIVETE_KEY
url = "https://api.kraken.com"
encode = 'utf8'


def sendPrivateRequest(path, pair=None, type=None, volume=None, leverage=None, ordertype=None, price=None):
    try:
        api_nonce = str(int(time.time()*1000))
        api_post = setParams(api_nonce=api_nonce, pair=pair, type=type, volume=volume,
                             leverage=leverage, ordertype=ordertype, price=price)

        api_path = '/0/private/' + path
        api_sha256 = hashlib.sha256(
            api_nonce.encode(encode) + api_post.encode(encode))
        api_hmac = hmac.new(base64.b64decode(api_key_private), api_path.encode(
            encode) + api_sha256.digest(), hashlib.sha512)
        api_signature = base64.b64encode(api_hmac.digest())

        api_request = urllib.request.Request(
            url + api_path, api_post.encode(encode))
        api_request.add_header('API-Key', api_key_public)
        api_request.add_header('API-Sign', api_signature)

        return load(api_request)

    except Exception as error:
        print('Failed private (%s)' % error)
        return {"open": []}


def sendPublicRequest(path, pair=None, interval=None, since=None):
    try:
        api_post = setParams(pair=pair, interval=interval,
                             since=since)

        api_path = '/0/public/' + path + '?' + api_post
        api_request = urllib.request.Request(
            url + api_path)

        return load(api_request)
    except Exception as error:
        print('Failed public (%s)' % error)
        return {"open": []}


def setParams(api_nonce=None, pair=None, type=None, volume=None, leverage=None, ordertype=None, price=None, interval=None, since=None):
    api_post = ""
    if (api_nonce != None):
        api_post = api_post + 'nonce=' + api_nonce
    if (pair != None):
        api_post = api_post + '&pair=' + pair
    if (type != None):
        api_post = api_post + '&type=' + type
    if (volume != None):
        api_post = api_post + '&volume=' + str(volume)
    if (leverage != None):
        api_post = api_post + '&leverage=' + str(leverage)
    if (ordertype != None):
        api_post = api_post + '&ordertype=' + ordertype
    if (price != None):
        api_post = api_post + '&price=' + str(price)
    if (interval != None):
        api_post = api_post + '&interval=' + str(interval)
    if (since != None):
        api_post = api_post + '&since=' + str(since)

    return api_post


def load(api_request):
    gcontext = ssl.SSLContext()
    api_response = urllib.request.urlopen(
        api_request, context=gcontext).read().decode()
    api_data = json.loads(api_response)

    return api_data['result']


def createOrder(params):
    logEnteredPosition = getters.getLogEnteredPosition(params)
    if logEnteredPosition == True:
        json_formatted_str = json.dumps(params, indent=2)
        log.info("entered position ")
        log.info(json_formatted_str)
