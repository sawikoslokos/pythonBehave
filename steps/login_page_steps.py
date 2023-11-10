from behave import When, Given, Then, Step
from pages.login_page import LoginPageUsername, LoginPagePassword
from utils.data_provider import DataProvider


login_page_username = LoginPageUsername()
login_page_password = LoginPagePassword()


@When('User login as {user}')
def step_impl(context, user):
    user_data = DataProvider.get_user_data(user)
    login_page_username.click(login_page_username.submitBtn)
    login_page_username.set_username(user_data.get('username'))
    login_page_username.submit()
    login_page_password.set_password(user_data.get("password"))
    login_page_username.submit()
