from selenium import webdriver
from password import Password

browser = webdriver.Chrome()
browser.get("https://github.com")

signin_link = browser.find_element_by_link_text("Sign in")
signin_link.click()

username_box = browser.find_element_by_id("login_field")
username_box.send_keys("1714605923@qq.com")

password = Password()
password_box = browser.find_element_by_id("password")
password_box.send_keys(password.password)
password_box.submit()

assert "JackSuuu" in browser.page_source
# check if we login to the correct account which we can check if it's correct using the assertion

# profile_link = browser.find_element_by_class_name("user-profile-link")
# link_label = profile_link.get_attribute("innerHTML")
# assert "JackSuuu" in link_label

browser.quit()