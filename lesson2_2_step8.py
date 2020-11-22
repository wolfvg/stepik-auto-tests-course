from selenium import webdriver
import os

import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://suninjuly.github.io/file_input.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
#    input2 = browser.find_element_by_id('treasure').valuex



 #   button = browser.find_element_by_tag_name("button")
 #   browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input1 = browser.find_element_by_name('firstname')
    input1.send_keys("Petr")

    input2 = browser.find_element_by_name('lastname')
    input2.send_keys("Petrov")

    input3 = browser.find_element_by_name('email')
    input3.send_keys("Pet@rov")

    current_dir = os.path.abspath(os.path.dirname(__file__))    # получаем путь к директории текущего исполняемого файла 
    file_path = os.path.join(current_dir, 'test.txt')           # добавляем к этому пути имя файла 

    input4 = browser.find_element_by_name('file')
    input4.send_keys(file_path)





#    input3 = browser.find_element_by_xpath('//input[@placeholder="Input your email"]')
#    input3.send_keys("Smol@ensk")

    # Отправляем заполненную форму
    button = browser.find_element_by_css_selector("button.btn")
    button.click()

    # Проверяем, что смогли зарегистрироваться
    # ждем загрузки страницы
  #  time.sleep(1)

    # находим элемент, содержащий текст

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()