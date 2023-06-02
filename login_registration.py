# import time
# from selenium import webdriver
# driver = webdriver.Chrome(executable_path='C:/chromedriver.exe')
# driver.maximize_window()
# driver.implicitly_wait(5)
# driver.get("https://practice.automationtesting.in/")
# my_account = driver.find_element_by_id("menu-item-50")
# my_account.click()
# email = driver.find_element_by_id("reg_email")
# email.send_keys("hyqakuzira@mailinator.com")
# password = driver.find_element_by_id("reg_password")
# password.send_keys("Zxcv12345!!!$%^")
# register = driver.find_element_by_name("register")
# register.click()
# driver.quit()

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
logout = driver.find_element_by_link_text("Logout")
logout_get_text = logout.text
assert logout_get_text == "Logout"
driver.quit()