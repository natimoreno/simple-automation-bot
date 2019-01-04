__author__ = "nmoreno"
__copyright__ = "Copyright (c) 2018 Monica Natalia Moreno"


class WebRunner(object):

    def __init__(self, driver):
        '''
        Constructor
        :param driver:
        :return:
        '''
        self.driver = driver

    def close(self):
        '''
        Close driver
        :return:
        '''
        self.driver.close()

    def navigate_url(self, url):
        '''
        Open a url
        :param url:
        :return:
        '''
        self.driver.get(url=url)

    def refresh(self):
        '''
        Refresh browser's content
        :return:
        '''
        self.driver.refresh()

    def write(self, by_type, by,  text):
        '''
        Write in element
        :param by_type:
        :param by:
        :param text:
        :return:
        '''
        web_element = self.driver.find_element(by_type, by)
        web_element.clear()
        web_element.send_keys(text)

    def click(self, by_type, by):
        '''
        Clic an element
        :param by_type:
        :param by:
        :return:
        '''
        web_element = self.driver.find_element(by_type, by)
        web_element.click()

    def find_elements(self, by_type, by):
        '''
        Find elements
        :param by_type:
        :param by:
        :return:
        '''
        return self.driver.find_elements(by_type, by)
