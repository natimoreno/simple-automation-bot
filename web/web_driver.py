from .chrome_webdriver import ChromeWebDriver
from .firefox_webdriver import FirefoxWebDriver

__author__ = "nmoreno"
__copyright__ = "Copyright (c) 2018 Monica Natalia Moreno"


class Browser:

    FIREFOX = 'Firefox'
    CHROME = 'Chrome'


class WebDriver:

    BROWSER_TABLE = {
        Browser.CHROME: ChromeWebDriver,
        Browser.FIREFOX: FirefoxWebDriver
    }

    @staticmethod
    def create_driver(browser):
        '''
        Create driver depending on browser
        :param browser:
        :return:
        '''
        if browser not in WebDriver.BROWSER_TABLE.keys():
            raise Exception()
        return WebDriver.BROWSER_TABLE[browser]()
