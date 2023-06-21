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


class Msg(Region):
    """
    Класс описывает страницу сообщений:
    содержит первое сверху сообщение
    """
    msg = Element(By.CSS_SELECTOR, '.msg-dialogs-item__content', 'Сообщения')


class SubMenu(Region):
    """
    Класс описывает дополнительное меню пункта "Контакты":
    содержит подпункт "Контакты"
    """
    contacts = Element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle', 'Контакты из доп.меню')


class ContextMenuDialog(Region):
    remove = Element(By.CSS_SELECTOR, '[title="Переместить"]', 'кнопка Переместить')


class WereRemoveDialog(Region):
    #folder_1 = Element(By.CSS_SELECTOR, '.', 'Корневая папка')
    folder_1 = Element(By.CSS_SELECTOR, '.controls-MoveDialog__title', 'Корневая папка')
    folder = Element(By.CSS_SELECTOR, '[title = "Папка для перемещения"]', 'Папка для перемещения')


class Close(Region):
    close = Element(By.CSS_SELECTOR, '.tags-base__close controls-icon_size-s', "Крестик")


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
        sleep(4)
        message.msg.context_click()
        sleep(10)
        context_menu_dialog = ContextMenuDialog(self.driver)
        context_menu_dialog.remove.click()
        sleep(1)
        were_remove = WereRemoveDialog(self.driver)
        were_remove.folder.click()
        sleep(3)
        message.msg.context_click()
        sleep(4)
        context_menu_dialog.remove.click()
        sleep(4)
        were_remove.folder_1.click()
        sleep(3)
