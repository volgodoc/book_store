# 4/8 тест: Shop: работа в корзине
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
driver.execute_script("window.scrollBy(0, 300);")

#Две книжки в корзину
WebAppDev_book = driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(1)
JS_Dt_Algrtm_book = driver.find_element_by_css_selector('[data-product_id="180"]').click()
time.sleep(1)

# Идем в корзину
Cart_page_lnk = driver.find_element_by_id('wpmenucartli').click()
time.sleep(2)

# Удаляем первую книгу WebAppDev_book и отменяем удаление
WebAppDev_book_del = driver.find_element_by_css_selector('a.remove[data-product_id="182"]').click()
time.sleep(2)

explicit_20 = WebDriverWait(driver, 20)
WebAppDev_book_undo_EC = explicit_20.until(
    EC.element_to_be_clickable((By.LINK_TEXT, 'Undo?'))).click()
time.sleep(2)

# Увекличиваю товар до 3ех, перед этим очистив поле .clear()
JS_Dt_Algrtm_book_count = driver.find_element_by_css_selector('tbody > tr:nth-child(1) input')
JS_Dt_Algrtm_book_count.clear()
time.sleep(1)
JS_Dt_Algrtm_book_count.send_keys("3")

# Обновляем корзину
UpBasket_btn = driver.find_element_by_css_selector('[value="Update Basket"]').click()
time.sleep(1)

# Проверяем через assert что value для книги JS ранво 3
Numeric_assrt = driver.find_element_by_css_selector('tbody > tr:nth-child(1) input')
Numeric_check = Numeric_assrt.get_attribute("value")
assert Numeric_check == "3"
print("Значение атрибута Value='" + str(Numeric_check) + "'")
time.sleep(3)

# Нажимаем на кнопку "APPLY COUPON"
AppCpon_btn = driver.find_element_by_name('apply_coupon').click()

# Проверяем текст "Please enter a coupon code."

Enter_cpon_code_txt = explicit_20.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "ul.woocommerce-error > li"), "Please enter a coupon code."))
print(Enter_cpon_code_txt)

Enter_cpon_code_wr = driver.find_element_by_css_selector('ul.woocommerce-error > li')
Enter_cpon_code_text = Enter_cpon_code_wr.text
assert "Please enter a coupon code." in Enter_cpon_code_text
print("Надпись в строчке предупреждения об ошибке: '" + str(Enter_cpon_code_text) + "'")

time.sleep(5)
# driver.quit()