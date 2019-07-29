import pytest
import unittest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

browser = webdriver.Chrome(ChromeDriverManager().install())

class MyTestCase(unittest.TestCase):
    def test_registration1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser.get(link)

        browser.find_element_by_class_name('form-control.first').send_keys('Имя')
        browser.find_element_by_css_selector('body > div > form > div.first_block > div.form-group.second_class > input').send_keys(
            'Фамилия')
        browser.find_element_by_class_name('form-control.third').send_keys('qqq@ww.ee')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!",  welcome_text, "Should be equal text")

    def test_registration2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser.get(link)

        browser.find_element_by_class_name('form-control.first').send_keys('Имя')
        browser.find_element_by_css_selector(
            'body > div > form > div.first_block > div.form-group.second_class > input').send_keys(
            'Фамилия')
        browser.find_element_by_class_name('form-control.third').send_keys('qqq@ww.ee')

        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        time.sleep(1)

        welcome_text_elt = browser.find_element_by_tag_name("h1")

        welcome_text = welcome_text_elt.text

        self.assertEqual("Поздравляем! Вы успешно зарегистировались!",  welcome_text, "Should be equal text")

if __name__ == '__main__':
    unittest.main()