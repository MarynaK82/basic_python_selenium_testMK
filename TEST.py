from selenium import webdriver
driver = webdriver.Chrome("/Users/marynakaminska/Downloads/chromedriver")
driver.get("https://www.wikipedia.org/")
search_field = driver.find_element_by_id("searchInput").send_keys("Test Automation")
search_button = driver.find_element_by_xpath("//form[@id = 'search-form']/fieldset/button")

search_field.send_keys("Test Automation")
search_button.click("//form[@id = 'search-form']/fieldset/button")
assert "Test automation" in driver.title
driver.quit()