from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from selenium.webdriver.support.ui import Select
import math
import os
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

browser = webdriver.Chrome(ChromeDriverManager().install())

link = "http://suninjuly.github.io/explicit_wait2.html"
browser.get(link)

WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "10000 RUR")
    )

browser.find_element_by_id('book').click()
x = int(browser.find_element_by_id('input_value').text)
y = str(math.log(abs(12*math.sin(int(x)))))

browser.find_element_by_id('answer').send_keys(y)

browser.find_element_by_id('solve').click()
#
# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
#
# x = int(browser.find_element_by_id('input_value').text)
# y = str(math.log(abs(12*math.sin(int(x)))))
#
# browser.find_element_by_id('answer').send_keys(y)
#
# browser.find_element_by_class_name('btn-primary').click()

# browser.find_element_by_name ('firstname').send_keys('Name')
# browser.find_element_by_name('lastname').send_keys('Lastname')
# browser.find_element_by_name('email').send_keys('Email@mail.ru')
#
# current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла
# file_path = os.path.join(current_dir, 'file.txt')           # добавляем к этому пути имя файла
# browser.find_element_by_id('file').send_keys(file_path)
# browser.find_element_by_class_name('btn-primary').click()

# x = int(browser.find_element_by_id('input_value').text)
# y = str(math.log(abs(12*math.sin(int(x)))))
#
# #browser.execute_script('return arguments[0].scrollIntoView(true);')
# browser.execute_script('window.scrollBy(0, 200);')
#
#
#
