# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
import unittest, time, re

class UntitledTestCase(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "https://www.katalon.com/"
        self.verificationErrors = []
        self.accept_next_alert = True
    
    def test_untitled_test_case(self):
        driver = self.driver
        driver.get("https://www.ticketland.ru/")
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='с 9:00 до 21:00'])[1]/preceding::a[2]").click()
        driver.find_element_by_name("LoginForm[contact]").clear()
        driver.find_element_by_name("LoginForm[contact]").send_keys("A.sidorova@ticketland.ru")
        driver.find_element_by_name("LoginForm[password]").clear()
        driver.find_element_by_name("LoginForm[password]").send_keys("Fhutynbyf971Co")
        driver.find_element_by_name("LoginForm[contact]").clear()
        driver.find_element_by_name("LoginForm[contact]").send_keys("a.sidorova@ticketland.ru")
        driver.find_element_by_xpath("(.//*[normalize-space(text()) and normalize-space(.)='*'])[2]/following::div[7]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Поиск'])[1]/following::div[7]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='с 9:00 до 21:00'])[1]/preceding::a[2]").click()
        driver.find_element_by_xpath(u"(.//*[normalize-space(text()) and normalize-space(.)='Мои акции'])[1]/following::b[1]").click()
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException as e: return False
        return True
    
    def is_alert_present(self):
        try: self.driver.switch_to_alert()
        except NoAlertPresentException as e: return False
        return True
    
    def close_alert_and_get_its_text(self):
        try:
            alert = self.driver.switch_to_alert()
            alert_text = alert.text
            if self.accept_next_alert:
                alert.accept()
            else:
                alert.dismiss()
            return alert_text
        finally: self.accept_next_alert = True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
