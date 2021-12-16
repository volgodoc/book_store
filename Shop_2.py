# 4/7 тест: Shop: отображение, скидка товара
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

#ходим на сайта
driver.get("http://practice.automationtesting.in/")
time.sleep(1)

# Вкладка My Acc-nt Mn - Вход: почта - пароль - Login
MyAccnt_UpMn = driver.find_element_by_link_text("My Account").click()
Mail_Area = driver.find_element_by_id("username").send_keys("retrapakko@vusra.com")
Pass_Area = driver.find_element_by_id("password").send_keys("tap@rj219011IoE_")
time.sleep(1)
Logn_btn = driver.find_element_by_css_selector('input[value="Login"]').click()
time.sleep(1)

# Вкладка Shop - Откр книгу "Android Quick Start Guide"
Shop_UpMn = driver.find_element_by_link_text("Shop").click()
time.sleep(1)
Android_QSG_book = driver.find_element_by_css_selector('img[alt="Android Quick Start Guide"]').click()
time.sleep(0.5)

# Проверка через assert содержимое старйо и акционной цены
explicit_20 = WebDriverWait(driver, 20)
Price_600 = explicit_20.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'del > span.woocommerce-Price-amount'), '₹600.00'))
print("₹600.00 - " + str(Price_600)) # True или None
Price_600_assrt = driver.find_element_by_css_selector('del > span.woocommerce-Price-amount')
Price_600_txt = Price_600_assrt.text
assert Price_600_txt == '₹600.00'

Price_450 = explicit_20.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'ins > span.woocommerce-Price-amount'), '₹450.00'))
print("₹450.00 - " + str(Price_450)) # True или None
Price_450_assrt = driver.find_element_by_css_selector('ins > span.woocommerce-Price-amount')
Price_450_txt = Price_450_assrt.text
assert Price_450_txt == '₹450.00'

# Нажимаем на обложку книги через ЕС
Android_QSG_EC = explicit_20.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'a img[alt="Android Quick Start Guide"]')))
Android_QSG_EC.click()
time.sleep(2)

# Закрываем окошко с картинкой через ЕС
Cross_cls_EC = explicit_20.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="pp_close"]')))
Cross_cls_EC.click()

time.sleep(5)
driver.quit()
