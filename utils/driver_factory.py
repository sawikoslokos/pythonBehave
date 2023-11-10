from threading import Lock
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service as ChromeService


class DriverMeta(type):
    _instances = {}

    _lock: Lock = Lock()

    def __call__(cls, *args, **kwargs):
        with cls._lock:
            if cls not in cls._instances:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


def create_driver(headless=False):
    options = _get_local_options(headless)
    service = ChromeService()
    driver = webdriver.Chrome(
        service=service,
        options=options
    )
    return driver


def _get_local_options(headless):
    options = Options()
    if headless:
        options.add_argument('--headless=new')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    options.add_argument('--allow-insecure-localhost')
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--remote-debugging-address=0.0.0.0')
    options.add_argument('--remote-debugging-port=9222')
    options.add_argument('--disable-gpu')
    options.add_argument('--window-size=1920,1080')
    options.add_argument('--disable-blink-features=AutomationControlled')
    return options


class DriverFactory(metaclass=DriverMeta):
    driver: webdriver = None

    def __init__(self):
        if self.driver is None:
            self.driver = create_driver()

    def get_driver(self):
        return self.driver