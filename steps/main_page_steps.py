from behave import When, Given, Then, Step
from pages.main_page import MainPage

main_page = MainPage()


@Step('User navigate to: {page_name} page')
def step_impl(context, page_name):
    main_page.select_from_sidebar(page_name)

@Step('User click on advanced button')
def step_impl(context):
    main_page.click_advanced()