# 4/9 тест: Shop: покупка товара
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(10)

# Ходим на сайта
driver.get("http://practice.automationtesting.in/")
time.sleep(1)

# Вкладка Shop и вниз 300px
Shop_UpMn = driver.find_element_by_link_text("Shop").click()
time.sleep(0.5)
driver.execute_script("window.scrollBy(0, 300);")
time.sleep(1)

# Добавил в корзину "HTML5 WebApp Development"
WebAppDev_book = driver.find_element_by_css_selector('[data-product_id="182"]').click()
time.sleep(2)

# Идем в корзину
explicit_20 = WebDriverWait(driver, 20)
Cart_page_lnk = explicit_20.until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'wpmenucart-contents'))).click()
time.sleep(2)

# Кликаем через ожидание на btn "Proceed to Checkout"
Proceed_t_checkout_EC = explicit_20.until(
    EC.element_to_be_clickable((By.CLASS_NAME, 'checkout-button'))).click()
time.sleep(3)

# Заполняем обязательные поля

FrstName_Area_EC = explicit_20.until(
    EC.element_to_be_clickable((By.ID, 'billing_first_name')))
# FrstName_Area_EC = driver.find_element_by_id("billing_first_name")
FrstName_Area_EC.send_keys("Mitrofan")
LastName_Area = driver.find_element_by_id("billing_last_name").send_keys("Priunilov")
I_Mail_Area = driver.find_element_by_id("billing_email").send_keys("mpri@betrust.com")
Phone_Area = driver.find_element_by_id("billing_phone").send_keys("79873775864")

time.sleep(0.5)
Country_Area = driver.find_element_by_id("s2id_billing_country").click()
Field_Country_Area = driver.find_element_by_id("s2id_autogen1_search").send_keys("Qatar")
Slct_Country_Area = driver.find_element_by_id("select2-results-1").click()
time.sleep(0.5)

Address_1_Area = driver.find_element_by_id("billing_address_1").send_keys("Gross Holl st.")
Address_2_Area = driver.find_element_by_id("billing_address_2").send_keys("502/8")
City_Area = driver.find_element_by_id("billing_city").send_keys("Livermore")
State_Area = driver.find_element_by_id("billing_state").send_keys("CA")
ZIP_Area = driver.find_element_by_id("billing_postcode").send_keys("94551")

# Выбираем способ оплаты "Check Payments" и крутим 600px down
driver.execute_script("window.scrollBy(0, 600);")
time.sleep(0.5)
Payments_check = driver.find_element_by_id("payment_method_cheque").click()
time.sleep(2)

# Прожимаем btn "PLACE ORDER"
Plc_ordr_btn = driver.find_element_by_id("place_order").click()
time.sleep(3)

# Используя явное ожидание, проверьте что отображается надпись "Thank you. Your order has been received."
Ordr_thank_txt = explicit_20.until(
    EC.text_to_be_present_in_element((By.CLASS_NAME, "woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
print("Надпись: --Thank you. Your order has been received.-- присутствует ли на странице? :", str(Ordr_thank_txt))
time.sleep(0.5)

# Используя явное ожидание, проверьте что в Payment Method отображается текст "Check Payments"
PayMtd_txt = explicit_20.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, "li.method > strong"), "Check Payments"))
print("Надпись: --Check Payments-- присутствует ли на странице? :", str(PayMtd_txt))

time.sleep(5)
# driver.quit()
