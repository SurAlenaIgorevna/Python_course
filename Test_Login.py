from selenium import webdriver
import unittest

def test_login(self, driver):
    driver = self.driver

    self.MainPage.open_home_page(driver)
    self.MainPage.login(username="a.sidorova@ticketland.ru", password="Fhutynbyf971Co")
