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

api_key_public = credentials.KRAKEN_API_KEY
api_key_private = credentials.KRAKEN_PRIVETE_KEY


def sendPrivateRequest(path, pair=None, type=None, volume=None, leverage=None, ordertype=None, price=None):
    try:
        api_nonce = str(int(time.time()*1000))
        api_post = 'nonce=' + api_nonce
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

        api_path = '/0/private/' + path
        api_sha256 = hashlib.sha256(
            api_nonce.encode('utf8') + api_post.encode('utf8'))
        api_hmac = hmac.new(base64.b64decode(api_key_private), api_path.encode(
            'utf8') + api_sha256.digest(), hashlib.sha512)
        api_signature = base64.b64encode(api_hmac.digest())

        api_request = urllib.request.Request(
            'https://api.kraken.com' + api_path, api_post.encode('utf8'))
        api_request.add_header('API-Key', api_key_public)
        api_request.add_header('API-Sign', api_signature)
        api_request.add_header(
            'User-Agent', 'Kraken trading bot example')
        api_response = urllib.request.urlopen(
            api_request).read().decode()
        api_data = json.loads(api_response)
        return api_data['result']

    except Exception as error:
        print('Failed (%s)' % error)


def sendPublicRequest(path, pair=None, interval=None, since=None):
    try:
        api_post = ''
        if (pair != None):
            api_post = api_post + '&pair=' + pair
        if (interval != None):
            api_post = api_post + '&interval=' + str(interval)
        if (since != None):
            api_post = api_post + '&since=' + str(since)

        api_path = '/0/public/' + path + '?' + api_post
        api_request = urllib.request.Request(
            'https://api.kraken.com' + api_path)
        api_request.add_header('User-Agent', 'Kraken trading bot example')
        api_response = urllib.request.urlopen(api_request).read().decode()
        api_data = json.loads(api_response)
        return api_data['result']
    except Exception as error:
        print('Failed (%s)' % error)
    return 0


def createOrder(params):
    logEnteredPosition = getters.getLogEnteredPosition(params)
    if logEnteredPosition == True:
        json_formatted_str = json.dumps(params, indent=2)
        log.info("entered position ")
        log.info(json_formatted_str)
