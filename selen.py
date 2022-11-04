from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import config
import time


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
    time.sleep(5)

    driver.get_screenshot_as_file('1.png')
    driver.save_screenshot('2.png')


    # assert "Python" in driver.title
    # elem = driver.find_element(By.NAME, "q")
    # elem.clear()
    # elem.send_keys("pycon")
    # elem.send_keys(Keys.RETURN)
    # assert "No results found." not in driver.page_source
except Exception as e:
    print(e)
finally:
    driver.close()





