from selenium import webdriver
import os
import time

import math
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try: 

  from selenium.webdriver.common.by import By
  from selenium.webdriver.support.ui import WebDriverWait
  from selenium.webdriver.support import expected_conditions as EC
  from selenium import webdriver

  browser = webdriver.Chrome()

  browser.get("http://suninjuly.github.io/wait2.html")

  # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
  button = WebDriverWait(browser, 5).until(
        EC.element_to_be_clickable((By.ID, "verify"))
      )
  button.click()
  message = browser.find_element_by_id("verify_message")

  assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()