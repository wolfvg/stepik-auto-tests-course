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

  browser.get("http://suninjuly.github.io/explicit_wait2.html")

  # говорим Selenium проверять в течение 5 секунд, пока кнопка не станет кликабельной
  text = WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element ((By.ID, "price"), '100')
      )


  button = browser.find_element_by_css_selector("button.btn")
  button.click()

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

  button = browser.find_element_by_id('solve')
  button.click()

  #button.click()
  #message = browser.find_element_by_id("verify_message")

  #assert "successful" in message.text

finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()