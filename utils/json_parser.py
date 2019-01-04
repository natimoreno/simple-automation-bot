import json

__author__ = "nmoreno"
__copyright__ = "Copyright (c) 2018 Monica Natalia Moreno"


def string_to_json(string):
    '''
    Convert string to json object
    :param string:
    :return:
    '''
    return json.loads(string)


def json_to_string(json_):
    '''
    Convert json object to string
    :param json_:
    :return:
    '''
    return str(json_)


def dic_to_json(dic):
    '''
    Convert dic to json object
    :param dic:
    :return:
    '''
    return json.loads(json.dumps(dic))
