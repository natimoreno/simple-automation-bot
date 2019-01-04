from selenium import webdriver
from .web_runner import WebRunner

__author__ = "nmoreno"
__copyright__ = "Copyright (c) 2018 Monica Natalia Moreno"


class ChromeWebDriver(object):

    def __init__(self):
        '''
        Constructor, here it recommends to initialize parameters
        :return:
        '''
        print('Initializing Chrome')

    @staticmethod
    def run():
        '''
        Return Web Runner with features from Selenium for Chrome driver
        :return:
        '''
        return WebRunner(webdriver.Chrome())
