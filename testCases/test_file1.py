import pytest

from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

from utilities.Logger import LogGenerator

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


class Test_Py:
    log = LogGenerator.loggen()

    def test_sum_001(self):  # item --> Test Case --> start with 'test_'
        self.log.debug("test_sum_001")
        self.log.info("test_sum_001")
        self.log.warning("test_sum_001")
        self.log.error("test_sum_001")
        self.log.critical("test_sum_001")
        a = 3
        b = 5
        sum = a + b
        print(sum)
        if sum == 8:
            self.log.info("test_sum_001 is Passed")
            print("test_sum_001 is Passed")
            assert True
        else:
            self.log.info("test_sum_001 is Failed")
            print("test_sum_001 is Failed")
            assert False

    # def test_mul_002(self):
    #     a = 3
    #     b = 5
    #     mul = a * b
    #     print(mul)
    #     if mul == 16:
    #         self.log.info("test_mul_002 is Passed")
    #         print("test_mul_002 is Passed")
    #         assert True
    #     else:
    #         self.log.info("test_mul_002 is Failed")
    #         print("test_mul_002 is Failed")
    #         assert False

    def sum_003(self):  # this item/function will not consider as testcase because of name
        a = 3
        b = 5
        sum = a + b
        print(sum)
        if sum == 16:
            print("test_mul_002 is Passed")
            assert True
        else:
            print("test_mul_002 is Failed")
            assert False

    #@pytest.mark.group1
    def test_Google(self):

        # driver = webdriver.Chrome()
        driver = webdriver.Chrome(options=chrome_options)
        driver.get("https://www.google.com/")
        logo = driver.find_element(By.CLASS_NAME, "lnXdpd").is_displayed()
        print(logo)
        if logo == True:
            driver.close()
            assert True  # test case status -->Pass
        else:
            driver.close()
            assert False  # test cases status --> Fail


# To run specific file's test cases
# pytest testCases/test_file1.py
# -v to show more details about test run
# pytest -v -m sanity
# -m you can run the specific test cases which are under sanity marker
