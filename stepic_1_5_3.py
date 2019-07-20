from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(ChromeDriverManager().install())
#DRIVER = 'Drivers\\chromedriver.exe'


LINK = 'http://suninjuly.github.io/registration2.html'

#driver = webdriver.Chrome(DRIVER)
driver.get(LINK)

try:
    elms = driver.find_elements_by_tag_name('input')
    for elm in elms:
        elm.send_keys('My Answer')

    button = driver.find_element_by_css_selector('.btn')
    button.click()

except Exception as exp:
    print("!!!!ERROR!!!!")
    print(exp)
    print("!!!!ERROR!!!!")
finally:
    time.sleep(5)
    driver.close()
    driver.quit()
