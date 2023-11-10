from .base_page import BasePage, PageMetaClass
from utils.data_decoder import DataDecoder
from utils.custom_wait import wait_until_page_load


class LoginPageUsername(BasePage):
    locators = {
        'login_input': ('ID', "input28"),
        "submit_Btn": ('XPATH', '//form//input[@type="submit"]'),
        "cpbn": ('ID', 'c-p-bn')
    }

    def set_username(self, username):
        self.login_input.set_text(username)

    def submit(self):
        if self.cpbn.is_displayed():
            self.click(self.cpbn)
        self.click(self.submit_Btn)
        wait_until_page_load()


class LoginPagePassword(LoginPageUsername, metaclass=PageMetaClass):
    locators = {
        'password_input': ('ID', "input53"),
    }

    def set_password(self, password):
        self.password_input.set_text(DataDecoder.decode_data(password))


