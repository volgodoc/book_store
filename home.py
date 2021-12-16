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

# Скролим вниз 600
driver.execute_script("window.scrollBy(0, 600);")

# Нажмите на название книги "Selenium Ruby"
Ttl_book_SeRb = driver.find_element_by_css_selector('a[href="http://practice.automationtesting.in/product/selenium-ruby/"] >h3').click()
time.sleep(1)

# Нажмите на вкладку "REVIEWS" (не смог почему то найти данную вкладку ни по text_link ни по частичному вхождению? ошибка и всё
# driver.find_element_by_partial_link_text("Rev").click()
# driver.find_element_by_link_text("Reviews (0)").click()
driver.execute_script("window.scrollBy(0, 300);")
Revws_tab = driver.find_element_by_css_selector('a[href="#tab-reviews"]').click()

# Пять звезд - поле - имя - почта - отправить.
Stars_5 = driver.find_element_by_class_name('star-5').click()
TxtArea = driver.find_element_by_id("comment").send_keys("Nice book!")
NameArea = driver.find_element_by_id("author").send_keys("Frodo")
MailArea = driver.find_element_by_id("email").send_keys("FrodoGood@mailinator.com")
Sub_btn = driver.find_element_by_id("submit").click()

time.sleep(3)
# driver.quit()

