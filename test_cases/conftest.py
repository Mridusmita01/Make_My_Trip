import pytest
import time
from selenium import webdriver
from Library.config import Config
from selenium.webdriver.firefox.options import Options

#Cross Browsing
firefox_path = r"C:\Users\HP\Desktop\driver_\geckodriver.exe"
@pytest.fixture(params=["Firefox","Chrome","Edge"])
def _driver(request):

    if request.param == "Firefox":
        options = Options()
        options.binary_location= r'C:\Program Files\Mozilla Firefox\firefox.exe'
        driver = webdriver.Firefox(executable_path=firefox_path,options=options)

    elif request.param == "Chrome":
        driver = webdriver.Chrome(Config.Chrome_path)
        time.sleep(10)

    elif request.param == "Edge":
        driver = webdriver.Edge(Config.Edge_path)

    driver.get(Config.Url)
    driver.maximize_window()
    driver.implicitly_wait(60)
    yield driver
    print(driver.title)
    # driver.save_screenshot("text_loginpage.png")
    driver.close()




