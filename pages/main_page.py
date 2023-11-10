from .base_page import BasePage
from seleniumpagefactory.Pagefactory import WebElement, By


class MainPage(BasePage):
    locators = {
        'sideBarMenu': ('XPATH', "//div[@data-testid='sidebar-draw']"),
        'advancedBtn': ('ID', "btn-search-advanced"),
        'profileBtn': ('ID',"navbar-btn-user-menu"),
        'profileDetailsBtn': ('ID', "navbar-link-profile"),
        'signOutBtn': ('ID', "navbar-link-signout")

    }

    sideBarMenu: WebElement

    def select_from_sidebar(self, menuitem : str):
        for element in self.sideBarMenu.find_elements(By.TAG_NAME, 'a'):
            if element.text.lower() == menuitem.lower():
                self.click(element)
                break

    def select_from_profile(self, item):
        self.click(self.profileBtn)
        if item == "Sign Out":
            self.click(self.signOutBtn)
        elif item == "Profile Details":
            self.click(self.profileDetailsBtn)

    def click_advanced(self):
        self.click(self.advancedBtn)