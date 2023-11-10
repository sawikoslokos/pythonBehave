from selenium.webdriver.support.ui import WebDriverWait
from utils.driver_factory import DriverFactory


def wait_until_page_load():
    WebDriverWait(driver=DriverFactory().get_driver(), timeout=20).until(
        lambda driver: 'complete' == driver.execute_script(
            'return document.readyState')
    )
