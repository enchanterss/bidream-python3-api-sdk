import hmac
import hashlib
import base64
import time
import datetime
from . import consts as c


def sign(message, secretKey):
    mac = hmac.new(bytes(secretKey, encoding='utf8'), bytes(message, encoding='utf8'), digestmod=hashlib.sha256)
    d = mac.digest()
    return base64.b64encode(d)


def pre_hash(timestamp, method, request_path, body):
    return str(timestamp) + str.upper(method) + request_path + body


def header(api_key, sign, timestamp, passphrase):
    header = dict()
    header[c.CONTENT_TYPE] = c.APPLICATION_JSON
    header[c.ACCESS_KEY] = api_key
    header[c.ACCESS_SIGN] = sign
    header[c.ACCESS_TIMESTAMP] = str(timestamp)
    header[c.ACCESS_PASSPHRASE] = passphrase
    return header


def parse_params_to_str(params):
    url = '?'
    for key, value in params.items():
        url = url + str(key) + '=' + str(value) + '&'

    return url[0:-1]


def get_timestamp():
    now = datetime.datetime.now()
    t = now.isoformat()
    return t + "Z"
