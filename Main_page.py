# -*- coding: utf-8 -*-
from selenium import webdriver
import unittest

class MainPage(webdriver):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True

    def open_home_page(self, driver):
            driver.get("https://www.ticketland.ru/")

    def login(self, driver, username, password):

            driver.find_element_by_xpath(
            u"(.//*[normalize-space(text()) and normalize-space(.)='с 9:00 до 21:00'])[1]/preceding::a[2]").click()
            driver.find_element_by_name("LoginForm[contact]").send_keys(username)
            driver.find_element_by_name("LoginForm[password]").send_keys(password)

    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()