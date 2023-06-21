from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from atf.ui import *
from atf import log, info


class AuthOnline(Region):
    """
    Класс описывает страницу авторизации:
    содержит текстовые поля логина и пароля
    """
    login_inp = TextField(By.CSS_SELECTOR, '[name = "Login"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '[name = "Password"]', 'пароль')


class MainOnline(Region):
    """
    Класс описывает раздел контакты:
    содержит пункт аккордеона "Контакты"
    """
    contacts = Element(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title', 'Контакты в аккордеоне')


class SubMenu(Region):
    """
    Класс описывает дополнительное меню пункта "Контакты":
    содержит подпункт "Контакты"
    """
    contacts = Element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle', 'Контакты из доп.меню')


class Msg(Region):
    """
    Класс описывает страницу сообщений:
    содержит первое сверху сообщение
    """
    msg = Element(By.CSS_SELECTOR, '.msg-dialogs-item__content', 'Сообщения')


class ContextMenuDialog(Region):
    mark = Element(By.CSS_SELECTOR, '[title="Пометить"]', 'кнопка Пометить')


class Tag(Region):
    tag = Element(By.CSS_SELECTOR, '.tags-base__name', 'тег')

class Test(TestCaseUI):
    """
    Содержит тест
    """

    def test(self):
        """
        Проводит на fix-online тест: отправление и удаление сообщения
        """
        driver = self.driver
        self.browser.open('http://fix-online.sbis.ru/')
        auth = AuthOnline(self.driver)
        auth.login_inp.type_in('куратор' + Keys.ENTER)
        auth.password_inp.type_in('пароль123' + Keys.ENTER)
        contact = MainOnline(self.driver)
        contact.contacts.click()
        sub_contact = SubMenu(self.driver)
        sub_contact.contacts.click()
        message = Msg(self.driver)
        sleep(6)
        message.msg.context_click()
        sleep(4)
        context_menu_dialog = ContextMenuDialog(self.driver)
        context_menu_dialog.mark.click()
        sleep(2)
        tag_etalon = Tag(self.driver)
        tag_etalon.tag.click()
        sleep(2)
        message.msg.context_click()
        sleep(4)
        context_menu_dialog.mark.click()
        sleep(2)
        tag_etalon.tag.click()
        sleep(2)

