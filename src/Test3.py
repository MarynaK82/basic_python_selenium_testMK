from selenium import webdriver
import time

driver = webdriver.Chrome("/Users/marynakaminska/Downloads/chromedriver")
driver.implicitly_wait(7)

driver.get("https://accounts.google.com")

create_account_button = driver.find_element_by_xpath("//*[text()='Створити обліковий запис']")
create_account_button.click()

time.sleep(2)

for_myself_button = driver.find_element_by_xpath("//*[text()='Для себе']")
for_myself_button.click()

email_list = ['55a.d', 'a@a', 'a@a.a']

validation_error2 = "Вибачте, але ім'я користувача має мати довжину від 6 до 30 символів."
validation_error1 = "Дозволені лише літери (a–z), числа (0–9) та крапки (.)."

user_dictionary = {'fn' : 'Maryna1', 'ln' : 'Kaminska1', 'password' : 'Abc123456789!'}

first_name_field = driver.find_element_by_id("firstName")
last_name_field = driver.find_element_by_id("lastName")
password_field = driver.find_element_by_name("Passwd")
conf_password_field = driver.find_element_by_name("ConfirmPasswd")
username_field = driver.find_element_by_id("username")
next_button = driver.find_element_by_id("accountDetailsNext")


first_name_field.send_keys(user_dictionary['fn'])
last_name_field.send_keys(user_dictionary['ln'])
password_field.send_keys(user_dictionary['password'])
conf_password_field.send_keys(user_dictionary['password'])


def validate_username_field(email):
    username_field.clear()
    username_field.send_keys(email)
    next_button.click()
    time.sleep(1)
    assert validation_error1 in driver.page_source

#for email in email_list:
 #  validate_username_field(email)

validate_username_field(email_list[1])
validate_username_field(email_list[2])



username_field.clear()
username_field.send_keys(email_list[0])
next_button.click()
time.sleep(1)
assert validation_error2 in driver.page_source


driver.quit()




