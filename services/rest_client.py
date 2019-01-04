import requests

__author__ = "nmoreno"
__copyright__ = "Copyright (c) 2018 Monica Natalia Moreno"


class RestClient:

    def __init__(self, ip, port=None, username=None, password=None):
        '''
        Constructor
        :param ip:
        :param port:
        :param username:
        :param password:
        :return:
        '''
        self.ip = ip
        self.port = port
        self.username = username
        self.password = password

    def get_request(self, uri=None, headers=None):
        '''
        Get request
        :param uri:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.get(url=uri, headers=headers)

    def get_request_params(self, uri, params, headers=None):
        '''
        Get request with params
        :param uri:
        :param params:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.get(url=uri, params=params, headers=headers)

    def get_request_data(self, uri, payload, headers=None):
        '''
        Get request with data
        :param uri:
        :param payload:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.get(url=uri, data=payload, headers=headers)

    def get_request_auth_and_params(self, uri, params, headers=None):
        '''
        Get request with params and authentication
        :param uri:
        :param params:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.get(url=uri, params=params, headers=headers, auth=(self.username, self.password))

    def get_request_auth_and_data(self, uri, payload, headers=None):
        '''
        Get request with data and authentication
        :param uri:
        :param payload:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.get(url=uri, data=payload, headers=headers, auth=(self.username, self.password))

    def post_request(self, uri=None, headers=None):
        '''
        Post request
        :param uri:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.post(url=uri, headers=headers)

    def post_request_params(self, uri, params, headers=None):
        '''
        Port request with params
        :param uri:
        :param params:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.post(url=uri, params=params, headers=headers)

    def post_request_data(self, uri, payload, headers=None):
        '''
        Post request with data
        :param uri:
        :param payload:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.post(url=uri, data=payload, headers=headers)

    def post_request_auth_and_params(self, uri, params, headers=None):
        '''
        Post request with params and authentication
        :param uri:
        :param params:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.post(url=uri, params=params, headers=headers, auth=(self.username, self.password))

    def post_request_auth_and_data(self, uri, payload, headers=None):
        '''
        Post request with data and authentication
        :param uri:
        :param payload:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.post(url=uri, data=payload, headers=headers, auth=(self.username, self.password))

    def put_request(self, uri=None, headers=None):
        '''
        Put request
        :param uri:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.put(url=uri, headers=headers)

    def put_request_params(self, uri, params, headers=None):
        '''
        Put request with params
        :param uri:
        :param params:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.put(url=uri, params=params, headers=headers)

    def put_request_data(self, uri, payload, headers=None):
        '''
        Put request with data
        :param uri:
        :param payload:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.put(url=uri, data=payload, headers=headers)

    def put_request_auth_and_params(self, uri, params, headers=None):
        '''
        Put request with params and authentication
        :param uri:
        :param params:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.put(url=uri, params=params, headers=headers, auth=(self.username, self.password))

    def put_request_auth_and_data(self, uri, payload, headers=None):
        '''
        Put request with data and authentication
        :param uri:
        :param payload:
        :param headers:
        :return:
        '''
        uri = ''.join([self.ip, uri])
        self._header_(uri, headers)
        return requests.put(url=uri, data=payload, headers=headers, auth=(self.username, self.password))

    def _header_(self, uri, headers=None):
        '''
        Print request data
        :param uri:
        :param headers:
        :return:
        '''
        print('Request to service {}'.format(uri))
        if headers is not None:
            print('Headers: {}'.format(headers))
