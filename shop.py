# Shop: отображение страницы товара  / Shop: количество товаров в категории
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
time.sleep(2)

# Вкладка Shop - Книга HTML5forms
Shop_UpMn = driver.find_element_by_link_text("Shop").click()
HTML5forms_book = driver.find_element_by_css_selector('img[alt="Mastering HTML5 Forms"]').click()

# Проверяем, что заголовок книги назвается: "HTML5 Forms"
explicit_20 = WebDriverWait(driver, 20)
Title_book = explicit_20.until(
    EC.text_to_be_present_in_element((By.CSS_SELECTOR, '#product-181 h1[itemprop="name"]'), "HTML5 Forms"))
print(Title_book)

Title_book_elmnt = driver.find_element_by_css_selector('#product-181 h1[itemprop="name"]')
Title_book_txt = Title_book_elmnt.text
assert "HTML5 Forms" in Title_book_txt
print("Заголовок книги называется: -" + str(Title_book_txt)+"-")
time.sleep(5)

# Следующий слайд переход в категорию товаров @HTML@
# 1. Проверка через значение количества в категории HTML в сайд баре
HTML_catgr = driver.find_element_by_link_text("HTML").click()
Count_catgr_sbar = driver.find_element_by_css_selector('li.cat-item-19 > span.count')
Count_catgr_txt = Count_catgr_sbar.text
print("В сайдбаре в категории --HTML-- отфильтрованы", str(Count_catgr_txt), "товара.")
# 2. Проверка через одинаковый class на самйо странице товаров в категории HTML
Count_catgr_page = driver.find_elements_by_css_selector('ul.products > li.product_cat-html')
if len(Count_catgr_page) == 3:
    print("На странице присутствует 3 товара из категории --HTML--")
else:
    print("Хм... А разве не 3 товара на странице? Тогда давайте посмотрим в сайдбаре, и сравним информацию.")

# driver.quit()