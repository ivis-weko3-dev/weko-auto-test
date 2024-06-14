# Generated by Selenium IDE
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from pathlib import Path

# 変数
base_url = "https://192.168.56.105"
base_save_folder = "screenshots/"
base_download_dir = "downloads/"
test_account_mail = "contributor@weko-selenium.jp"
test_account_password = "uspass123"
guest_mail = "guest@weko-selenium.jp"

term_title = 'Test Terms and Conditions Title'
edited_term_title = 'Edited ' + term_title

users = {
    'System': {
        'mail': 'sysadmin@weko-selenium.jp',
        'password': 'uspass123'
    },
    'Repository': {
        'mail': 'repoadmin@weko-selenium.jp',
        'password': 'uspass123'
    },
    'Community': {
        'mail': 'comadmin@weko-selenium.jp',
        'password': 'uspass123'
    },
    'RegCon': {
        'mail': 'reg-contributor@weko-selenium.jp',
        'password': 'uspass123'
    },
    'NoRegCon': {
        'mail': 'noreg-contributor@weko-selenium.jp',
        'password': 'uspass123'
    },
    'PrxRegCon': {
        'mail': 'prxreg-contributor@weko-selenium.jp',
        'password': 'uspass123'
    },
    'General': {
        'mail': 'general@weko-selenium.jp',
        'password': 'uspass123'
    }
}

class SetupDriver:
    def setup_driver(self):
        options = webdriver.ChromeOptions()
        
        dldir_path = Path(base_download_dir)
        dldir_path.mkdir(exist_ok=True)
        download_dir = str(dldir_path.resolve())
        # print(download_dir)


        options.add_experimental_option("prefs", {
            "download.default_directory": download_dir,
            "plugins.always_open_pdf_externally": True
        })

        self.driver = webdriver.Remote(
            command_executor="http://selenium:4444/wd/hub", options=options
        )
        self.vars = {}

        self.driver.implicitly_wait(10)
        
        self.driver.get(base_url)
        self.driver.find_element(By.XPATH,"/html/body/div/div[2]/button[3]").click()
        self.driver.find_element(By.XPATH,"/html/body/div/div[3]/p[2]/a").click()

    def teardown_method(self):
        self.driver.quit()
