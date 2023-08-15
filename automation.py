from pathlib import Path
from selenium import webdriver
from datetime import datetime
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from playsound import playsound
from selenium.webdriver.support import expected_conditions as EC




class autmated_visa_appointment:
    def __init__(self, base_img : Path):
        self.base_img = base_img
    
    def main(self):
        options = Options()
        options.add_argument('--disable-blink-features=AutomationControlled')
        options.add_argument("--headless=new")
        options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), 
                                options = options)
        driver.maximize_window()
        driver.get("https://www.seine-saint-denis.gouv.fr/booking/create/9636/0")
        time.sleep(5)

        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        path01 = './test_images/' + dt_string + '.png'
        driver.save_screenshot(path01)
        driver.find_element("xpath","//input[@type='checkbox']").click()
    

        driver.find_element("xpath","//input[@type='submit']").click()
        time.sleep(5)

        now = datetime.now()
        dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
        path01 = './test_images/' + dt_string + '.png'
        driver.save_screenshot(path01)  
        driver.close()


        def validate_file_contents(file1, file2):
            with open(file1, 'rb') as f1, open(file2, 'rb') as f2:
                contents1 = f1.read()
                contents2 = f2.read()
            rslt=  contents1 == contents2
            return rslt

        rslt= validate_file_contents(path01, self.base_img)

        return rslt


