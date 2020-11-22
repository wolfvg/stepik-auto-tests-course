from selenium import webdriver
import time

import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 
    link = "http://SunInJuly.github.io/execute_script.html"
    browser = webdriver.Chrome()
    browser.get(link)

    # Ваш код, который заполняет обязательные поля
#    input2 = browser.find_element_by_id('treasure').valuex


    x =  browser.find_element_by_id('input_value').text
    y=calc(x) 
    print(y)

 #   button = browser.find_element_by_tag_name("button")
 #   browser.execute_script("return arguments[0].scrollIntoView(true);", button)

    input1 = browser.find_element_by_id('answer')
    input1.send_keys(y)


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