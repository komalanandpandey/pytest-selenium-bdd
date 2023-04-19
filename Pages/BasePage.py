from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.action_chains import ActionChains as AC


class BasePage:

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        return self.driver.title
        

    def do_click(self,by_locator):
        try:
            element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
            element.click
        except WebDriverException:
            print("Element is not clickable")
         
    def hover_and_click(self,element):
        try:
            a = AC(self.driver)
            a.move_to_element(element).click().perform()
        except WebDriverException:
            print("Element is not Clickable")    

    def enter_text(self,by_locator,text):
         element = WebDriverWait(self.driver,10).until(EC.visibility_of_element_located(by_locator))
         element.send_keys(text)     