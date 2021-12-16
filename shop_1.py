# 4/6 тест: Shop: сортировка товаров
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

# Вкладка Shop
Shop_UpMn = driver.find_element_by_link_text("Shop").click()
time.sleep(1)

# Проверка, что в селекторе --Default sorting-- пункт по умолчанию
select_deflt = driver.find_element_by_css_selector("[value='menu_order']")
select_deflt_selected = select_deflt.get_attribute("selected")
print("Выбран ли в селекторе пункт --Default sorting--?: ", select_deflt_selected)
if select_deflt_selected is not None: # то есть, -да)
    print("Да, селектрор стоит на --Default sorting-- ")
else:
    print("Нет, сортировка по умолчанию не выбрана.")
time.sleep(1)

# Селектор от больешго к меньшему
More_to_less_slct = driver.find_element_by_tag_name("select")
select_Mr_t_Lss = Select(More_to_less_slct)
select_Mr_t_Lss.select_by_value("price-desc")
time.sleep(2)
print("Теперь отсортируем товары от большей цены к меньшей и проведем проверку результата.")

# Проверка, что выбрано: Селектор от больешго к меньшему
select_H_t_L = driver.find_element_by_css_selector("[value='price-desc']")
select_H_t_L_selected = select_H_t_L.get_attribute("selected")
print("Выбран ли сейчас в селекторе пункт --Sort by price: high to low--?: ", select_H_t_L_selected)
if select_H_t_L_selected is None: # то есть -нет)
    print("Нет, селектор --Sort by price: high to low-- не сработал.")
else:
    print("Да, теперь страница отсортирована согласно селектрора --Sort by price: high to low--")
time.sleep(1)

# driver.quit()