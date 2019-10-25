from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait

class BasePage():

    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator):
        expected_conditions - ec.presence_of_element_located(locator)
        return WebDriverWait(self.driver, 10).until(expected_conditions, message="unable to locate element")






    def login(self):
        self.driver.find_element_by_xpath("//button[@type='submit']").click()
        WebDriverWait(self.driver)


