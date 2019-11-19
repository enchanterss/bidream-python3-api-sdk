import requests
import json
from . import consts as c, utils, excps
import time


class Client(object):
    # param use_server_time's value is True, request will use server timestamp
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time, api_url):

        self.session = requests.Session()
        self.API_KEY = api_key
        self.API_SECRET_KEY = api_secret_key
        self.PASSPHRASE = passphrase
        self.use_server_time = use_server_time
        self.api_url = api_url

    def _request(self, method, request_path, params, cursor=False):
        
        # request_url
        if method == c.GET:
            request_path = request_path + utils.parse_params_to_str(params)
        url = self.api_url + request_path

        # timestamp
        timestamp = utils.get_timestamp()
        if self.use_server_time:
            timestamp = self._get_timestamp()

        # sign
        body = "" if method == c.GET else json.dumps(params)
        sign = utils.sign(utils.pre_hash(timestamp, method, request_path, str(body)), self.API_SECRET_KEY)

        # header
        header = utils.header(self.API_KEY, sign, timestamp, self.PASSPHRASE)

        # send request
        start = time.time()
        response = None
        if method == c.GET:
            response = self.session.get(url, headers=header)
        elif method == c.POST:
            response = self.session.post(url, data=body, headers=header)
        elif method == c.DELETE:
            response = self.session.delete(url, data=body, headers=header)
        end = time.time()
        print("response time: " + str(end-start) + " s")

        # exception handle
        if not str(response.status_code).startswith('2'):
            raise excps.APIException(response)
        else:
            print("seccess.")
        try:
            res_header = response.headers
            if cursor:
                r = dict()
                try:
                    r['before'] = res_header['BEFORE'] if "BEFORE" in res_header.keys() else res_header['CB_BEFORE']
                    r['after'] = res_header['AFTER'] if "AFTER" in res_header.keys() else res_header['CB_AFTER']
                except:
                    print("Invalid pagination error message: ", r)
                return response.json(), r
            else:
                return response.json()
        except ValueError:
            if not response.text == '':
                return response.text
            else:
                return 'Query the result by calling get_order_info'

    def _request_without_params(self, method, request_path):
        return self._request(method, request_path, {})

    def _request_with_params(self, method, request_path, params, cursor=False):
        return self._request(method, request_path, params, cursor)

    def _get_timestamp(self):
        url = self.api_url + c.SERVER_TIMESTAMP
        response = self.session.get(url)
        if response.status_code == 200:
            return response.json()['iso']
        else:
            return ""




