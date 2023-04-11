import time
from loguru import logger

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

from bot.misc import Config, get_root_dir


options = Options()
# options.add_argument('--headless')
prefs = {'download.default_directory' : f"{get_root_dir()}/temp"}
options.add_experimental_option('prefs', prefs)

driver = webdriver.Chrome(chrome_options=options)


def download_matrix(user_name: str, user_date: str, user_gender: str) -> None:
    logger.info(f"Loading {Config.MATRIX_PARSE_URL}")
    try:
        driver.get(Config.MATRIX_PARSE_URL)

        # Find elements
        name = driver.find_element(By.XPATH, '//*[@id="name"]')
        date = driver.find_element(By.XPATH, '//*[@id="dob"]')
        gender = Select(driver.find_element(By.XPATH, '//*[@id="gender"]'))
        calc = driver.find_element(By.XPATH, '/html/body/div[2]/main/section[2]/div/'
                                             'div[1]/div[2]/section/div/div[1]/form/input')
        download = driver.find_element(By.XPATH, '/html/body/div[2]/main/section[2]/div'
                                                 '/div[1]/div[2]/section/div/div[2]/div[5]/a')

        # Send Keys
        name.send_keys(user_name)
        date.send_keys(user_date)
        gender.select_by_index(0 if user_gender == "Женский" else 1)
        time.sleep(1)
        calc.submit()

        # Download
        time.sleep(5)
        download.click()
    except Exception:
        logger.error(Exception)
