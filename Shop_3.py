# 4/8 тест: Shop: проверка цены в корзине
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

# Вкладка Shop
Shop_UpMn = driver.find_element_by_link_text("Shop").click()
time.sleep(1)
driver.execute_script("window.scrollBy(0, 150);")

#Книжку в корзинку
WebAppDev_book = driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(2)

# Проверка цены и штучности в корзине на странице товара
Cart_contnts_assrt = driver.find_element_by_class_name('cartcontents')
Cart_contnts_txt = Cart_contnts_assrt.text
assert Cart_contnts_txt == '1 Item'

Price_180_assrt = driver.find_element_by_css_selector('span[class="amount"]')
Price_180_txt = Price_180_assrt.text
assert Price_180_txt == '₹180.00'
print(str(Cart_contnts_txt), "-", str(Price_180_txt))

# Идем в корзину
Cart_page_lnk = driver.find_element_by_id('wpmenucartli').click()

# Стоимость в Subtotal и Total через ЕС
Subtotal_180_assrt = driver.find_element_by_css_selector('td[data-title="Subtotal"] > span[class="woocommerce-Price-amount amount"]')
Subtotal_180_txt = Subtotal_180_assrt.text
assert Subtotal_180_txt == '₹180.00'
print("Subtotal: ", str(Subtotal_180_txt))

Total_end_189_assrt = driver.find_element_by_css_selector('tr.order-total span.amount')
Total_end_189_txt = Total_end_189_assrt.text
assert Total_end_189_txt == '₹189.00'
print("Total: ", str(Total_end_189_txt) + ", including roaming tax of delivery to Russia.")

time.sleep(5)
# driver.quit()