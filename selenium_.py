from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import config
import time
from functions import file_name


try:
    if config.web_browser == 'Chrome':
        driver = webdriver.Chrome(executable_path=config.web_driver_path)
    elif config.web_browser == 'Firefox':
        driver = webdriver.Firefox(executable_path=config.web_driver_path)
    elif config.web_browser == 'Safari':
        driver = webdriver.Safari(executable_path=config.web_driver_path)
    elif config.web_browser == 'Edge':
        driver = webdriver.Edge(executable_path=config.web_driver_path)

    driver.get(config.site_adr)
    time.sleep(3)
    # fill in the first page of the form: firstname and lastname
    firstname_input = driver.find_element(By.NAME, "name")
    # clear the form - to be sure it is empty
    firstname_input.clear()
    firstname_input.send_keys('al')
    lastname_input = driver.find_element(By.NAME, "lastname")
    lastname_input.clear()
    lastname_input.send_keys('v')
    time.sleep(1)
    click_next_1 = driver.find_element(By.CLASS_NAME, "b24-form-btn").click()
    time.sleep(2)

    # fill in second form page: email and phone number
    email_input = driver.find_element(By.NAME, "email")
    email_input.clear()
    email_input.send_keys('al@al.com')
    phone_imput = driver.find_element(By.NAME, "phone")
    phone_imput.clear()
    phone_imput.send_keys('123456')
    time.sleep(1)
    click_next_2 = driver.find_element(By.XPATH, "/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[3]/div[2]/button").click()
    time.sleep(2)

    # fill in third page of the form: date of birth
    date_input = driver.find_element(By.XPATH, "/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[2]/div/div/div/div/div[1]/input")

    #driver.execute_script("arguments[0].setAttribute('value', '20.08.2022')", date_input)
    #driver.execute_script("arguments[0].value = arguments[1]", date_input, '20.08.2022')
    # the form has "readonly" attribute, so we need to change it before sending keys:
    driver.execute_script("arguments[0].removeAttribute('readonly','readonly')", date_input)
    date_input.send_keys('20.08.2022')
    time.sleep(1)
    click_next_3 = driver.find_element(By.XPATH, "/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[4]/div[2]/button").click()

    time.sleep(80)



    # «YYYY-MM-DD_HH:mm_<user id>.jpg»
    driver.get_screenshot_as_file(f'{config.screenshots_dir}_date and time _user_id.jpg')
    driver.save_screenshot(f'{config.screenshots_dir}_user_id.jpg')



except Exception as e:
    print(e)
finally:
    driver.close()





