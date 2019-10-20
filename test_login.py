from selenium import webdriver
from login_page import LoginPage

driver = webdriver.Chrome("/Users/marynakaminska/Downloads/chromedriver")
driver.get("https://www.instagram.com/accounts/login/")

login_page = LoginPage(driver)
login_page.enter_username("sozdai")
login_page.enter_password("1234567")
login_page.login()
