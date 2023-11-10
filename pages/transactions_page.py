from base_page import PageMetaClass
from main_page import MainPage


class TransactionsPage(MainPage, metaclass=PageMetaClass):
    locators = {
        'submit_Btn': ('ID', "submit")
    }
