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

# Вкладка My Acc-nt Mn - регистрация: почта - пароль - Input
MyAccnt_UpMn = driver.find_element_by_link_text("My Account")
MyAccnt_UpMn.click()
time.sleep(1)
Mail_reg_Area = driver.find_element_by_id("reg_email").send_keys("121retrapakko@vusra.com")
Pass_reg_Area = driver.find_element_by_id("reg_password").send_keys("121tap@rj219011IoE_")
time.sleep(2)
explicit_20 = WebDriverWait(driver, 20)
Reg_btn_EC = explicit_20.until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, 'input[value="Register"]'))).click()
# Reg_btn = driver.find_element_by_css_selector('input[value="Register"]').click()
time.sleep(2)

# Разлогин после регистрации , что бы отработать залогин в след слайде
LogoAut_lnk = driver.find_element_by_link_text("Sign out").click()
time.sleep(2)

# Вход: почта - пароль - Login
Mail_Area = driver.find_element_by_id("username").send_keys("111retrapakko@vusra.com")
Pass_Area = driver.find_element_by_id("password").send_keys("111tap@rj219011IoE_")
time.sleep(1)
Logn_btn = driver.find_element_by_css_selector('input[value="Login"]').click()

# Проверка элемента Logout на странице
# explicit_20 = WebDriverWait(driver, 20)
Logout_lnk = explicit_20.until(
    EC.visibility_of_element_located((By.LINK_TEXT, "Logout")))
if Logout_lnk is None: # если элемента НЕТ
    print("Элемент --Logout-- отсутствует на странице")
else:
    print("Элемент --Logout-- в наличие на странице")

time.sleep(3)
driver.quit()
