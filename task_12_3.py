from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from atf.ui import *
from atf import log, info


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '[name = "Login"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '[name = "Password"]', 'пароль')


class Test(TestCaseUI):
    def test(self):
        driver = self.driver
        self.browser.open('http://fix-online.sbis.ru/')
        auth = AuthOnline(self.driver)
        auth.login_inp.type_in('куратор' + Keys.ENTER)
        auth.password_inp.type_in('пароль123' + Keys.ENTER)
        sleep(3)
        driver.switch_to.new_window()
        self.browser.open('http://fix-online.sbis.ru/opendoc.html?guid=28b89ff0-81b4-4329-afbe-eb59e453fa9c&client=6255711')
        sleep(4)
