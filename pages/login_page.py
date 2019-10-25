from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page import BasePage

class LoginPage():

    def __init__(self, driver):
        self.driver = driver

    def enter_username(self, username):
        self.driver.find_element_by_name("username").clear()
        self.driver.find_element_by_name("username").send.keys(username)

    def enter_password(self, password):
        self.driver.find_element_by_name("password").clear()
        self.driver.find_element_by_name("password").send.keys(password)

    def login(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click()




