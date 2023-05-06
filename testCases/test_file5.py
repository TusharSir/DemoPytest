import time

import pytest


import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver
from selenium.webdriver.support.select import Select

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")

@pytest.mark.group1
def test_Google():
    #driver = webdriver.Firefox()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://www.google.com/")
    logo = driver.find_element(By.CLASS_NAME, "lnXdpd").is_displayed()
    driver.find_element(By.XPATH, "//textarea[@id='APjFqb']").send_keys("Credence IT Professional Training Institute")
    driver.find_element(By.XPATH, "//img[@alt='Google']").click()
    driver.find_element(By.XPATH, "//div[@class='FPdoLc lJ9FBc']//input[@name='btnK']").click()
    print(logo)
    if logo == True:
        driver.close()
        assert True  # test case status -->Pass
    else:
        driver.close()
        assert False  # test cases status --> Fail
