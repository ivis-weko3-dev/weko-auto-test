import pytest
import time

import config
from methods_required_during_testing import logout
from selenium.webdriver.common.by import By

@pytest.fixture()
def driver():
    setup_driver = config.SetupDriver()
    setup_driver.setup_driver()
    setup_driver.driver.execute_script('window.scroll(0, 0)')
    time.sleep(1)
    setup_driver.driver.find_element(
        By.XPATH,
        '//*[@id="klaro"]/div/div/div/div/div/button'
    ).click()
    yield setup_driver.driver
    logout(setup_driver.driver)
    setup_driver.teardown_method()
    time.sleep(1)
