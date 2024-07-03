import inspect
import os
import time

import config
from methods_required_during_testing import *

# pytest shell_test/test_secret_url_three_days.py::TestPreparation
class TestPreparation:
    """Prepare for tests(No.19, 25, 43, 49)"""
    # pytest shell_test/test_secret_url_three_days.py::TestPreparation::test_no_19
    def test_no_19(self, enable_secret_url):
        """Prepare for test No.19
        
        Secret URL is enabled
        Expiration Date is 3
        Download Limit is 3
        Access Setting is Open Date and publish date is after today
        User's Role is Repository Administrator
        
        Args:
            enable_secret_url(WebDriver): WebDriver object
        """
        # log in as Repository Administrator
        login(enable_secret_url, 'Repository')

        # search target item
        search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

        # display content's info
        click_file_information_button(enable_secret_url)

        # click secret url button
        A7(enable_secret_url)

        # get secret url from email and create a file to store it
        url = get_secret_url(config.users['Repository']['mail'].split('@', 1)[0])
        with open(config.base_secret_url_dir + 'secret_url_19.txt', 'w', encoding='utf-8') as f:
            f.write(url)

    # pytest shell_test/test_secret_url_three_days.py::TestPreparation::test_no_25
    def test_no_25(self, enable_secret_url):
        """Prepare for test No.25

        Secret URL is enabled
        Expiration Date is 3
        Download Limit is 3
        Access Setting is Open Date and publish date is after today
        User's Role is Contributor and the item's owner

        Args:
            enable_secret_url(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(enable_secret_url, 'RegCon')

        # search target item
        search_and_display_target_item(enable_secret_url, config.item_name_dic['before_publish'])

        # display content's info
        click_file_information_button(enable_secret_url)

        # click secret url button
        A7(enable_secret_url)

        # get secret url from email and create a file to store it
        url = get_secret_url(config.users['RegCon']['mail'].split('@', 1)[0])
        with open(config.base_secret_url_dir + 'secret_url_25.txt', 'w', encoding='utf-8') as f:
            f.write(url)

    # pytest shell_test/test_secret_url_three_days.py::TestPreparation::test_no_43
    def test_no_43(self, enable_secret_url):
        """Prepare for test No.43

        Secret URL is enabled
        Expiration Date is 3
        Download Limit is 3
        Access Setting is Private
        User's Role is Repository Administrator

        Args:
            enable_secret_url(WebDriver): WebDriver object
        """
        # log in as Repository Administrator
        login(enable_secret_url, 'Repository')

        # search target item
        search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

        # display content's info
        click_file_information_button(enable_secret_url)

        # click secret url button
        A7(enable_secret_url)

        # get secret url from email and create a file to store it
        url = get_secret_url(config.users['Repository']['mail'].split('@', 1)[0])
        with open(config.base_secret_url_dir + 'secret_url_43.txt', 'w', encoding='utf-8') as f:
            f.write(url)

    # pytest shell_test/test_secret_url_three_days.py::TestPreparation::test_no_49
    def test_no_49(self, enable_secret_url):
        """Prepare for test No.49

        Secret URL is enabled
        Expiration Date is 3
        Download Limit is 3
        Access Setting is Private
        User's Role is Contributor and the item's owner

        Args:
            enable_secret_url(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(enable_secret_url, 'RegCon')

        # search target item
        search_and_display_target_item(enable_secret_url, config.item_name_dic['private'])

        # display content's info
        click_file_information_button(enable_secret_url)

        # click secret url button
        A7(enable_secret_url)

        # get secret url from email and create a file to store it
        url = get_secret_url(config.users['RegCon']['mail'].split('@', 1)[0])
        with open(config.base_secret_url_dir + 'secret_url_49.txt', 'w', encoding='utf-8') as f:
            f.write(url)

# pytest shell_test/test_secret_url_three_days.py::TestExecution
class TestExecution:
    """Execute tests(No.19, 25, 43, 49)"""
    # pytest shell_test/test_secret_url_three_days.py::TestExecution::test_no_19
    def test_no_19(self, driver):
        """Execute test No.19
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # get secret url from file
        with open(config.base_secret_url_dir + 'secret_url_19.txt', 'r', encoding='utf-8') as f:
            url = f.read()

        # access secret url
        driver.get(url)
        time.sleep(1)

        # check download deadline passed error message
        check_download_deadline_passed_error_message(driver)

        # check if the file is not downloaded
        file_list = os.listdir(config.base_download_dir)
        assert 'before_publish.txt' not in file_list

        save_screenshot(driver, inspect.currentframe().f_code.co_name)

        os.remove(config.base_secret_url_dir + 'secret_url_19.txt')

    # pytest shell_test/test_secret_url_three_days.py::TestExecution::test_no_25
    def test_no_25(self, driver):
        """Execute test No.25

        Args:
            driver(WebDriver): WebDriver object
        """
        # get secret url from file
        with open(config.base_secret_url_dir + 'secret_url_25.txt', 'r', encoding='utf-8') as f:
            url = f.read()

        # access secret url
        driver.get(url)
        time.sleep(1)

        # check download deadline passed error message
        check_download_deadline_passed_error_message(driver)

        # check if the file is not downloaded
        file_list = os.listdir(config.base_download_dir)
        assert 'before_publish.txt' not in file_list

        save_screenshot(driver, inspect.currentframe().f_code.co_name)

        os.remove(config.base_secret_url_dir + 'secret_url_25.txt')

    # pytest shell_test/test_secret_url_three_days.py::TestExecution::test_no_43
    def test_no_43(self, driver):
        """Execute test No.43

        Args:
            driver(WebDriver): WebDriver object
        """
        # get secret url from file
        with open(config.base_secret_url_dir + 'secret_url_43.txt', 'r', encoding='utf-8') as f:
            url = f.read()

        # access secret url
        driver.get(url)
        time.sleep(1)

        # check download deadline passed error message
        check_download_deadline_passed_error_message(driver)

        # check if the file is not downloaded
        file_list = os.listdir(config.base_download_dir)
        assert 'private.txt' not in file_list

        save_screenshot(driver, inspect.currentframe().f_code.co_name)

        os.remove(config.base_secret_url_dir + 'secret_url_43.txt')

    # pytest shell_test/test_secret_url_three_days.py::TestExecution::test_no_49
    def test_no_49(self, driver):
        """Execute test No.49

        Args:
            driver(WebDriver): WebDriver object
        """
        # get secret url from file
        with open(config.base_secret_url_dir + 'secret_url_49.txt', 'r', encoding='utf-8') as f:
            url = f.read()

        # access secret url
        driver.get(url)
        time.sleep(1)

        # check download deadline passed error message
        check_download_deadline_passed_error_message(driver)

        # check if the file is not downloaded
        file_list = os.listdir(config.base_download_dir)
        assert 'private.txt' not in file_list

        save_screenshot(driver, inspect.currentframe().f_code.co_name)

        os.remove(config.base_secret_url_dir + 'secret_url_49.txt')

def login(driver, target_key):
    """Log in as target user
    
    Args:
        driver(WebDriver): WebDriver object
        target_key(str): target user's key in config
    """
    # set login_user from config
    login_user = config.users[target_key]
    # log in as target user
    A1(driver, login_user['mail'], login_user['password'])

def get_secret_url(user: str):
    """Get secret URL
    
    Args:
        user(str): user's role
        
    Returns:
        str: secret URL
    """
    mail_list = os.listdir('mail/' + user + '/new')

    with open('mail/' + user + '/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        text = f.read()
        url = re.search('https://.*', text).group()
        return url

def check_download_deadline_passed_error_message(driver):
    """Check if the error message for download deadline passed is displayed
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

    # check error message
    error_message = error_page[0].find_element(By.XPATH, './/div/div/h1')
    assert error_message.text == 'The expiration date for download has been exceeded.', \
        'Error message is not "The expiration date for download has been exceeded."'

def save_screenshot(driver, co_name):
    """Save screenshot
    
    Args:
        driver(WebDriver): WebDriver object
        co_name(str): test case name
    """
    time.sleep(1)
    driver.save_screenshot(
        config.base_save_folder + 'secret_url/' + d + "_" + co_name + ".png")
