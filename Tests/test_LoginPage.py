
import pytest
from Tests.test_Base import BaseTest
from Config.config import TestData
from Pages.LoginPage import LoginPage
import base64

class Test_login(BaseTest):

    def test_login_page_title(self):
        self.loginPage = LoginPage(self.driver)
        page_title = self.loginPage.get_login_page_title()
        print(page_title)
       # assert self.page_title == TestData.PAGE_TITLE

    def test_click_on_blog(self):
        self.loginPage = LoginPage(self.driver)
        #self.loginPage.click_on_blog(LoginPage.BLOG_LINK)


    def test_login_to_app(self):
        self.loginPage = LoginPage(self.driver)
        decrypt_password=base64.b64decode(TestData.PASSWORD).decode("ascii")
        self.loginPage.login_to_app(TestData.USER_NAME,decrypt_password)    
     
