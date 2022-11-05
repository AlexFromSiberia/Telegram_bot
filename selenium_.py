from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
import config
import time
import sql


def run_selenium():
    """
    Fills registration form with User data: ('firstname',
    'lastname', 'e_mail', 'phone_number', 'birth_date').
    Saves screenshot with name in format «YYYY-MM-DD_HH:mm_<user id>.jpg».
    """
    # Gets user data from data base
    user_data = sql.get_user_data()
    if user_data == 0:
        pass
    else:
        # Run selenium
        try:
            # choose the right driver for use (check config.py file)
            s = Service(config.web_driver_path)
            if config.web_browser == 'Chrome':
                driver = webdriver.Chrome(service=s)
            elif config.web_browser == 'Firefox':
                driver = webdriver.Firefox(service=s)
            elif config.web_browser == 'Safari':
                driver = webdriver.Safari(service=s)
            elif config.web_browser == 'Edge':
                driver = webdriver.Edge(service=s)

            # open registration form
            driver.get(config.site_adr)
            time.sleep(3)
            # fill in the first page of the form: firstname and lastname
            firstname_input = driver.find_element(By.NAME, "name")
            # clear the form - to be sure it is empty
            firstname_input.clear()
            firstname_input.send_keys(user_data[1])
            time.sleep(1)

            lastname_input = driver.find_element(By.NAME, "lastname")
            lastname_input.clear()
            lastname_input.send_keys(user_data[2])
            time.sleep(1)
            click_next_1 = driver.find_element(By.CLASS_NAME, "b24-form-btn").click()
            time.sleep(2)

            # fill in second form page: email and phone number
            email_input = driver.find_element(By.NAME, "email")
            email_input.clear()
            email_input.send_keys(user_data[3])
            phone_imput = driver.find_element(By.NAME, "phone")
            phone_imput.clear()
            phone_imput.send_keys(user_data[4])
            time.sleep(1)
            click_next_2 = driver.find_element(By.XPATH,
                                               "/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[3]/div[2]/button").click()
            time.sleep(2)

            # fill in third page of the form: date of birth
            date_input = driver.find_element(By.XPATH,
                                             "/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[2]/div/div/div/div/div[1]/input")

            # the form has "readonly" attribute, so we need to change it before sending keys:
            driver.execute_script("arguments[0].removeAttribute('readonly','readonly')", date_input)
            date_input.send_keys(user_data[5])
            time.sleep(1)
            # click_next_3 = driver.find_element(By.XPATH, "/html/body/main/div/section/div/div/div/div/div/div/div/div/div[2]/form/div[4]/div[2]/button").click()
            time.sleep(2)

            # saving screenshot with name in format «YYYY-MM-DD_HH:mm_<user id>.jpg»
            driver.get_screenshot_as_file(f'{user_data[7]}')
            time.sleep(1)
        except Exception as e:
            print(e)
        finally:
            driver.close()



