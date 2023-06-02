# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username = driver.find_element_by_id("username")
# username.send_keys("hyqakuzira@mailinator.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Zxcv12345!!!$%^")
# login = driver.find_element_by_name("login")
# login.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# book5forms = driver.find_element_by_css_selector(".post-181 > .button.product_type_simple")
# book5forms.click()
# title = driver.find_element_by_tag_name("h1.product_title")
# title_get_text = title.text
# assert "HTML5 Forms" in title_get_text
# driver.quit()

# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username = driver.find_element_by_id("username")
# username.send_keys("hyqakuzira@mailinator.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Zxcv12345!!!$%^")
# login = driver.find_element_by_name("login")
# login.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# html_btn = driver.find_element_by_css_selector(".cat-item-19 > a")
# html_btn.click()
# items_count = driver.find_elements_by_class_name("product_cat-html")
# if len(items_count) == 3:
#     print("На странице 3 товара")
# else:
#     print("Ошибка"+ str(len(items_count)))
# driver.quit()

# from selenium import webdriver
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# username = driver.find_element_by_id("username")
# username.send_keys("hyqakuzira@mailinator.com")
# password = driver.find_element_by_id("password")
# password.send_keys("Zxcv12345!!!$%^")
# login = driver.find_element_by_name("login")
# login.click()
# shop = driver.find_element_by_link_text("Shop")
# shop.click()
# sorting = driver.find_element_by_name("orderby")
# sorting_default = sorting.get_attribute("value")
# if sorting_default == "menu_order":
#     print("Выбрано значение menu_order")
# else:
#     print("Выбрано другое значение")
# select = Select(sorting)
# select.select_by_value("price-desc")
# sorting = driver.find_element_by_name("orderby")
# select = Select(sorting)
# select.select_by_value("menu_order")
# sorting = driver.find_element_by_name("orderby")
# sorting_desc = sorting.get_attribute("value")
# if sorting_desc == "price-desc":
#     print("Выбрано значение price-desc")
# else:
#     print("Выбрано другое значение")
# driver.quit()

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://practice.automationtesting.in/")
my_account = driver.find_element_by_id("menu-item-50")
my_account.click()
username = driver.find_element_by_id("username")
username.send_keys("hyqakuzira@mailinator.com")
password = driver.find_element_by_id("password")
password.send_keys("Zxcv12345!!!$%^")
login = driver.find_element_by_name("login")
login.click()
shop = driver.find_element_by_link_text("Shop")
shop.click()
android_open = driver.find_element_by_css_selector(".post-169 .button")
android_open.click()
book_old_price = driver.find_element_by_css_selector(".price > del > span")
book_old_price_text = book_old_price.text
assert book_old_price_text == "₹600.00"
book_new_price = driver.find_element_by_css_selector("ins > span")
book_new_price_text = book_new_price.text
assert book_new_price_text == "₹450.00"
book_cover = WebDriverWait(driver, 5).until(
    EC.element_to_be_clickable((By.CSS_SELECTOR, ".images > a")))
book_cover.click()
cover_close = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.CLASS_NAME, "pp_close")))
cover_close.click()
driver.quit()

