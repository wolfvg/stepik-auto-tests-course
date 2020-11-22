from selenium import webdriver
import os
import time

import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 

   browser = webdriver.Chrome()
   browser.get("http://suninjuly.github.io/wait1.html")
   # говорим WebDriver искать каждый элемент в течение 5 секунд
   browser.implicitly_wait(5)

   button = browser.find_element_by_id("verify")
   button.click()
   message = browser.find_element_by_id("verify_message")

   assert "successful" in message.text
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()