# coding=utf-8

class APIException(Exception):
    def __init__(self, response):
        print(response.text + ', ' + str(response.status_code))
        self.code = 0
        try:
            json_res = response.json()
        except ValueError:
            self.message = 'Invalid JSON error message: '.format(response.text)
        else:
            if "msg" in json_res.keys() or "message" in json_res.keys():
                self.code = json_res['code'] if "code" in json_res.keys() else response.status_code
                self.message = json_res['msg'] if "msg" in json_res.keys() else json_res['message']
            else:
                self.code = 'None'
                self.message = 'Server error'

        self.status_code = response.status_code
        self.response = response
        self.request = getattr(response, 'request', None)

    def __str__(self):
        return 'API Request Error(code=%s): %s' % (self.code, self.message)

