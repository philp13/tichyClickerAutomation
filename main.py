import os
from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from time import sleep
from requestium import Session, Keys


class Clicker_Automation:
    def __init__(self):
        self.website = "tichy.clicker"
        self.profile = webdriver.FirefoxProfile()
        self.profile.set_preference("general.useragent.override",
                               'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:104.0) Gecko/20100101 Firefox/104.0 ')
        self.session = Session(webdriver_path='./chromedriver',
                          browser='chrome',
                          default_timeout=15)

    def start_clicker(self):
        self.session.driver.get(self.website)
        sleep(5)


if __name__ == '__main__':
    clicker = Clicker_Automation()
    clicker.start_clicker()
