import pytest
import time

import config

@pytest.fixture()
def driver():
    setup_driver = config.SetupDriver()
    setup_driver.setup_driver()
    setup_driver.driver.execute_script('window.scroll(0, 0)')
    time.sleep(1)
    yield setup_driver.driver
    setup_driver.teardown_method()
    time.sleep(1)
