from selenium import webdriver
from time import sleep
from selenium.webdriver import Keys, ActionChains
from selenium.webdriver.common.by import By
from atf.ui import *
from atf import log, info





#driver = webdriver.Chrome(sbis_site = 'http://fix-online.sbis.ru/'
#class MainSbisRu(Region):


class AuthOnline(Region):
    login_inp = TextField(By.CSS_SELECTOR, '[name = "Login"]', 'логин')
    password_inp = TextField(By.CSS_SELECTOR, '[name = "Password"]', 'пароль')

class MainOnline(Region):
    contacts = Element(By.CSS_SELECTOR, '.NavigationPanels-Accordion__title', 'Контакты в аккордеоне')

class Msg(Region):
    msg = Element(By.CSS_SELECTOR, '.msg-dialogs-item__content', 'Сообщения')
class SubMenu(Region):
    contacts = Element(By.CSS_SELECTOR, '.NavigationPanels-SubMenu__headTitle', 'Контакты из доп.меню')

class Text(Region):
    text = Element(By.CSS_SELECTOR, '.textEditor_slate_Field', 'Поле ввода сообщения')
    #but = Element(By.CSS_SELECTOR, 'controls-Button__icon', 'Отправить')
    but = Element(By.CSS_SELECTOR, '[class="controls-Button__icon controls-BaseButton__icon controls-icon_size-s controls-icon_style-contrast controls-icon icon-BtArrow"]', 'ищем кнопку')

class LastMsg(Region):
    text = CustomList(By.CSS_SELECTOR, '[class="msg-entity-text msg-entity_font_croppless richEditor_richContentRender_fontSize-m_theme-default controls_RichEditor_theme-default richEditor_richContentRender_theme-default richEditor_richContentRender richEditor_richContentRender_lineHeight-s richEditor_richContentRender_colorPalette-first richEditor_richContentRender_readOnly msg-entity-layout__text   "]', 'отправленное сообщение')


class MenuMsg(Region):
    mm = CustomList(By.CSS_SELECTOR, '[class="ws-ellipsis controls-Menu__content-wrapper_width"]', 'кнопка Удалить')


class YesNo(Region):
    yes = Element(By.CSS_SELECTOR, '[class="controls-BaseButton__text controls-Button__text_clickable_bg-same controls-Button__text_viewMode-outlined"]', 'Да')

class Test(TestCaseUI):
    def test(self):
        driver = self.driver

        self.browser.open('http://fix-online.sbis.ru/')
        auth = AuthOnline(self.driver)
        auth.login_inp.type_in('куратор'+Keys.ENTER)
        auth.password_inp.type_in('пароль123' + Keys.ENTER)
        contact = MainOnline(self.driver)
        contact.contacts.click()
        sub_contact = SubMenu(self.driver)
        sub_contact.contacts.click()
        message = Msg(self.driver)
        message.msg.click()
        message_text = Text(self.driver)
        message_text.text.type_in('Случайный текст')
        message_text.but.click()
        message.msg.click()
        last_msg = LastMsg(self.driver)
        sleep(2)
        #last_msg.text[len(last_msg.text)].context_click()
        last_msg.text.item(last_msg.text.size).context_click()
        #last_msg.text.item(1).mouse_over()
        #self.browser.refresh()
        sleep(2)
        button_dlt = MenuMsg(self.driver)
        button_dlt.mm.item(button_dlt.mm.size).click()
        y = YesNo(self.driver)
        y.yes.click()
        sleep(4)
        #print(button_dlt.mm.size)



# login = driver.find_element(By.CSS_SELECTOR, '[name = "Login"]')
# login.send_keys('куратор', Keys.ENTER)
# sleep(3)
# password = driver.find_element(By.CSS_SELECTOR, '[name = "Password"]')
# password.send_keys('пароль123', Keys.ENTER)
# sleep(7)
# class Test