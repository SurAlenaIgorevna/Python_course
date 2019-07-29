import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import math

browser = webdriver.Chrome(ChromeDriverManager().install())

def test_first_link():
    browser.implicitly_wait(2)
    browser.get("https://stepik.org/lesson/236895/step/1")
    browser.find_elements_by_class_name('navbar__auth')[0].click()
    browser.find_element_by_id('id_login_email').send_keys('sur.alena.igorevna@gmail.com')
    browser.find_element_by_id('id_login_password').send_keys('Fhutynbyf971Co')
    browser.find_element_by_class_name('sign-form__btn').click()
    time.sleep(3)

    answer = str(math.log(int(time.time())))
    browser.find_element_by_css_selector('textarea').send_keys(answer)
    browser.find_element_by_class_name('submit-submission').click()

    assert "Correct!" in browser.find_element_by_class_name('smart-hints__hint').text, "Нет сообщения об успехе!"

@pytest.mark.parametrize('link', [
#"https://stepik.org/lesson/236895/step/1",
"https://stepik.org/lesson/236896/step/1",
"https://stepik.org/lesson/236897/step/1",
"https://stepik.org/lesson/236898/step/1",
"https://stepik.org/lesson/236899/step/1",
"https://stepik.org/lesson/236903/step/1",
"https://stepik.org/lesson/236904/step/1",
"https://stepik.org/lesson/236905/step/1",
])
def test_other_links(link):
    browser.implicitly_wait(2)
    browser.get(link)

    answer = str(math.log(int(time.time())))
    browser.find_element_by_css_selector('textarea').send_keys(answer)
    browser.find_element_by_class_name('submit-submission').click()

    assert "Correct!" in browser.find_element_by_class_name('smart-hints__hint').text, browser.find_element_by_class_name('smart-hints__hint').text
