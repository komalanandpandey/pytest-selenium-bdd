import pytest
import sys
import time
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from Config.config import TestData
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options as FFO  #Need aliase otherwise chrome will not work

""" 
sys.stdout = sys.stderr   #Used to show console print output 
User below comman to run tests:
pytest Tests/test_LoginPage.py -v -s -n 3 --html=report/test-execution-report.html
 -v = Verbose output
 -s = to show console print output, bedefault python will not show any print("something") output
 -n 3 = number of threds e.g. 3 
 --html = path/to/report/name
"""

@pytest.fixture(params=["chrome","firefox"], scope='class') 
def init_driver(request):  #The request used to tell the test function use chrome & firefox at class level.
    #sys.stdout = sys.stderr  
        #OR use logging as below: 
    logger = logging.getLogger("Ayushyogi-qa logger")
    c_handler = logging.StreamHandler()
    logger.addHandler(c_handler)
    logger.setLevel(logging.DEBUG) #other options INFO, WARNING,ERROR,CRITICAL
    
    if request.param == "chrome":
        logger.debug("<=========Initializing Chrome Driver=========>")
        chrome_options = Options()
        chrome_options.add_argument("--allow-running-insecure-content")
        chrome_options.add_argument("--headless")
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install())
        ,options=chrome_options)
        driver.get(TestData.BASE_URL)
        driver.maximize_window()
        time.sleep(3)
    if request.param == "firefox":
        logger.info("=========Initializing Firefox Driver=========")
        firfox_options = FFO()   
        firfox_options.add_argument("--allow-running-insecure-content")
        firfox_options.add_argument("--headless")
        driver = webdriver.Firefox(service=Service(GeckoDriverManager().install())
        ,options=firfox_options)
        driver.get(TestData.BASE_URL)
        driver.maximize_window()
    request.cls.driver = driver
    yield
    logger.setLevel(logging.INFO)  #Can change log level at any place
    logger.info("<=========Tearing Down {} Driver =========>".format((driver.name).upper()))
    driver.quit()
