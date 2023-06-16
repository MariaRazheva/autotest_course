from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from atf.ui import *
from atf import log, info

class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '[name = "Login"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '[name = "Password"]', 'пароль')


class MainOnline(Region):
    vkladki = CustomList(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title', 'Контакты в аккордеоне')

class SubMenu(Region):
    tasks = Element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle', 'Контакты из доп.меню')


class Folders(Region):
    folders = CustomList(By.CSS_SELECTOR, '[class="ws-flexbox ws-flex-nowrap ws-flex-grow-1 ws-ellipsis ws-align-items-center"]', 'папки')
    button_plus = Element(By.CSS_SELECTOR, '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-m controls-icon_style-default controls-icon icon-RoundPlus"]', 'плюс')


class SubMenuPlus(Region):
    options = CustomList(By.CSS_SELECTOR, '[class="edws-AddButtonItem ws-flexbox ws-align-items-center ws-ellipsis"]', 'кнопки меню')


class FolderName(Region):
    namefield = Element(By.CSS_SELECTOR, '[class="controls-Field js-controls-Field controls-InputBase__nativeField controls-InputBase__nativeField_caretFilled controls-InputBase__nativeField_caretFilled_theme_default   controls-InputBase__nativeField_hideCustomPlaceholder"]', 'поле ввода')
    save = Element(By.CSS_SELECTOR, '[class="controls-BaseButton__text controls-Button__text_clickable_bg-same controls-Button__text_viewMode-outlined"]', 'сохранить')


class MenuTask(Region):
    mt = CustomList(By.CSS_SELECTOR, '[class="ws-ellipsis controls-Menu__content-wrapper_width"]', 'доп.меню для задач')


class YesNo(Region):
    yes = Element(By.CSS_SELECTOR, '[class="controls-BaseButton__text controls-Button__text_clickable_bg-same controls-Button__text_viewMode-outlined"]', 'Да')


class Test(TestCaseUI):
    def test(self):
        driver = self.driver
        self.browser.open('http://fix-online.sbis.ru/')
        auth = AuthOnline(self.driver)
        auth.login_inp.type_in('куратор' + Keys.ENTER)
        auth.password_inp.type_in('пароль123' + Keys.ENTER)
        main_page = MainOnline(self.driver)
        main_page.vkladki.item(2).click()
        submenu = SubMenu(self.driver)
        submenu.tasks.click()
        listfolders = Folders(self.driver)
        listfolders.folders.item(2).click()
        sleep(2)
        listfolders.folders.item(1).click()
        listfolders.button_plus.click()
        sleep(3)
        list_sub_buttons = SubMenuPlus(self.driver)
        list_sub_buttons.options.item(list_sub_buttons.options.size).click()
        name_folder = FolderName(self.driver)
        name_folder.namefield.type_in('Новая папка')
        name_folder.save.click()
        sleep(3)
        listfolders_2 = Folders(self.driver)
        listfolders_2.folders.item(listfolders_2.folders.size).click()
        listfolders_2.folders.item(listfolders_2.folders.size).context_click()
        sub_menu_task = MenuTask(self.driver)
        sub_menu_task.mt.item(2).click()
        y = YesNo(self.driver)
        y.yes.click()
        sleep(3)