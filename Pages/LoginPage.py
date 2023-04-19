from Pages.BasePage import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains as AC
from selenium.common.exceptions import WebDriverException
import time


class LoginPage(BasePage):

    """ Page locators """
    USER_NAME = (By.ID, "username")
    PASSWORD = (By.ID, "password")
    LOGIN_BUTTON =  "//button[@id='loginBtn']"

    #SIGN_UP_LINK = (By.Link_Text, "Sign up")

    """ Page Constructor """
    def __init__(self, driver):
        super().__init__(driver)

    """ Page Functions """
    def get_login_page_title(self):
        return self.get_page_title()
    
    def login_to_app(self, username, password):
        self.enter_text(self.USER_NAME, username)
        self.enter_text(self.PASSWORD, password)
        time.sleep(2)
        btn_login_elem = self.driver.find_element("xpath",self.LOGIN_BUTTON)
        self.hover_and_click(btn_login_elem)
        time.sleep(5)
        print(self.driver.current_url)
        assert "https://app.hubspot.com/login/confirm-to-login" in self.driver.current_url 
        time.sleep(5)


    def click_on_blog(self,by_locator):
        self.do_click(by_locator)
        time.sleep(5)    
    

    


