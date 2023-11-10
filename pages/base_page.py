from seleniumpagefactory import PageFactory
from utils.driver_factory import DriverFactory
from seleniumpagefactory.Pagefactory import WebElement
from utils.logger import custom_logger as cl


class PageMetaClass(type):
    def __new__(cls, name, bases, namespace, **kwargs):
        bases[0].locators.update(namespace['locators'])
        return type.__new__(cls, name, bases, dict(namespace))


class BasePage(PageFactory):
    log = cl()

    def __init__(self):
        super().__init__()
        self.driver = DriverFactory().get_driver()
        self.log.info("Startuje Drivera")

    def click(self, element: WebElement):
        self.log.info("Clicking element")
        element.click()
