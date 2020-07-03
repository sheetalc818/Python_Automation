import os
import time
import unittest

from selenium import webdriver


class FundooTest(unittest.TestCase):

    def setUp(self):  # This Function is executed before every test execution
        self.driver = webdriver.Chrome()

    def test_login(self):
        driver = self.driver

        driver.maximize_window()
        driver.get('https://fundoopush-dev.bridgelabz.com/login')

        driver.implicitly_wait(10)
        driver.find_element_by_id("mat-input-0").send_keys("Enter use id here")
        driver.find_element_by_id("mat-input-1").send_keys("123456")
        driver.find_element_by_class_name("mat-button-wrapper").click()
        time.sleep(10)

        # Click on Plus icon
        driver.find_element_by_class_name("plus-div").click()

        # Click on Add Article
        driver.find_element_by_xpath("//button[contains(text(),'ADD ARTICLE')]").click()
        time.sleep(10)

        # Add Title
        driver.find_element_by_xpath("//textarea[@placeholder='Title']").send_keys("Python Automation")
        time.sleep(5)

        # Click on add media
        driver.find_element_by_class_name("addMedia").click()
        time.sleep(5)

        #  Click on Redirect button
        driver.find_element_by_xpath("//div[4]//img[1]").click()
        time.sleep(5)

        # Add Redirect link
        driver.find_element_by_xpath("//input[@id='mat-input-3']").send_keys(
            "https://www.youtube.com/watch?v=itrgje2oqqU")
        time.sleep(5)

        # Click on done
        driver.find_element_by_xpath("//span[@class='mat-button-wrapper']").click()
        time.sleep(5)

        # Add Description
        driver.find_element_by_xpath("//div[@class='ql-editor ql-blank']").send_keys("written script in Python")
        time.sleep(5)

        # Upload Image
        elm = driver.find_element_by_xpath("//div[@class='quill-style']")
        elm.send_keys(os.getcwd() + "/Pictures/Wallpapers/alvo_fak.jpg")
        time.sleep(10)


if __name__ == '__main__':
    unittest.main()
