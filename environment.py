from utils.driver_factory import DriverFactory
from utils.custom_wait import wait_until_page_load
import os


def before_all(context):
    DriverFactory()
    # temporary solution to set up for test framework purpose
    os.environ["PRIVATE_KEY"] = "7FhgDn9eDIZnYZe7KObrAXA0AaPl6jhSMgYLqArDbE8="
    DriverFactory().get_driver().get('https://prestage.portal.trustpayments.dev')
    wait_until_page_load()
