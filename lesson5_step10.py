from selenium import webdriver
import time

browser = webdriver.Chrome()
link = "http://suninjuly.github.io/registration2.html"
browser.get(link)

browser.find_element_by_class_name('form-control.first').send_keys('Имя')
browser.find_element_by_css_selector('div.first_block > div.form-group.second_class > input').send_keys('Фамилия')
browser.find_element_by_class_name('form-control.third').send_keys('qqq@ww.ee')

# Отправляем заполненную форму
button = browser.find_element_by_css_selector("button.btn")
button.click()

# Проверяем, что смогли зарегистрироваться
# ждем загрузки страницы
time.sleep(1)

# находим элемент, содержащий текст
welcome_text_elt = browser.find_element_by_tag_name("h1")
# записываем в переменную welcome_text текст из элемента welcome_text_elt
welcome_text = welcome_text_elt.text

# с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
assert "Поздравляем! Вы успешно зарегистировались!" == welcome_text