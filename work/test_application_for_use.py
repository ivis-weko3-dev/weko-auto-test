import base64
import inspect
import os
import quopri

import config
from methods_required_during_testing import *

# pytest test_application_for_use.py::TestScenario1
class TestScenario1:
    """Test Scenario 1
    
    Requirements for items to be used:
        - The Providing Method is terms_of_use_only
        - The Providing Role is General
        - The Terms and Conditions are voluntary
    """
    # pytest test_application_for_use.py::TestScenario1::test_scenario_1_1
    def test_scenario_1_1(self, driver):
        """Test Scenario 1-1
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's owner

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(driver, 'RegCon')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ1')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_1.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert check_mail(config.users['RegCon']['mail'], 'テストシナリオ1')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_1.txt')

    # pytest test_application_for_use.py::TestScenario1::test_scenario_1_2
    def test_scenario_1_2(self, driver):
        """Test Scenario 1-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ1')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. The error message appears.
        apply_button.click()
        time.sleep(3)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_2")

    # pytest test_application_for_use.py::TestScenario1::test_scenario_1_3
    def test_scenario_1_3(self, driver):
        """Test Scenario 1-3
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's contributor
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(driver, 'PrxRegCon')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ1')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_1.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert check_mail(config.users['PrxRegCon']['mail'], 'テストシナリオ1')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_1.txt')

    # pytest test_application_for_use.py::TestScenario1::test_scenario_1_4
    def test_scenario_1_4(self, driver):
        """Test Scenario 1-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ1')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. The error message appears.
        apply_button.click()
        time.sleep(3)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_2")

    # pytest test_application_for_use.py::TestScenario1::test_scenario_1_5
    def test_scenario_1_5(self, driver):
        """Test Scenario 1-5
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.
        4. Not working before checking the box.
        5. Registered content is downloaded.
        6. No "Request for register Data Usage Report" email is sent to the applicant.

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ1')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(3)
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        header = modal.find_element(By.XPATH, './/*[@id="exampleModalLongTitle"]')
        terms = modal.find_element(By.XPATH, './/*[@id="terms"]')
        assert header.text == 'Terms and Conditions'
        assert terms.text == '利用規約のみ\nGeneral'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_2")

        # 3. The print dialog appears.
        print_button = modal.find_element(By.XPATH, './/*[@id="print-btn"]')
        print_button.click()
        time.sleep(3)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_3")
        # reload page for close print dialog
        driver.switch_to.window(window_handles[0])
        time.sleep(3)
        driver.refresh()
        time.sleep(3)

        # 4. Not working before checking the box.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        apply_button.click()
        time.sleep(3)
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert not 'test_scenario_1.txt' in file_list

        # 5. Registered content is downloaded.
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(3)
        next_btn.click()
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_1.txt' in file_list

        # 6. No "Request for register Data Usage Report" email is sent to the applicant.
        assert check_mail(config.users['General']['mail'], 'テストシナリオ1')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_1.txt')

    # pytest test_application_for_use.py::TestScenario1::test_scenario_1_6
    def test_scenario_1_6(self, driver):
        """Test Scenario 1-6
        
        1. Transition to the login page
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # 1. Transition to the login page
        search_and_display_target_item(driver, 'テストシナリオ1')
        check_login_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

# pytest test_application_for_use.py::TestScenario2
class TestScenario2:
    """Test Scenario 2
    
    Requirements for item to be used:
        - The Providing Method is terms_of_use_only
        - The Providing Role is Guest
        - The Terms and Conditions are voluntary
    """
    # pytest test_application_for_use.py::TestScenario2::test_scenario_2_1
    def test_scenario_2_1(self, driver):
        """Test Scenario 2-1
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(driver, 'RegCon')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ2')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_2.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert check_mail(config.users['RegCon']['mail'], 'テストシナリオ2')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_2.txt')

    # pytest test_application_for_use.py::TestScenario2::test_scenario_2_2
    def test_scenario_2_2(self, driver):
        """Test Scenario 2-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ2')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. The error message appears.
        apply_button.click()
        time.sleep(3)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_2")

    # pytest test_application_for_use.py::TestScenario2::test_scenario_2_3
    def test_scenario_2_3(self, driver):
        """Test Scenario 2-3
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's contributor
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(driver, 'PrxRegCon')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ2')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_2.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert check_mail(config.users['PrxRegCon']['mail'], 'テストシナリオ2')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_2.txt')
    
    # pytest test_application_for_use.py::TestScenario2::test_scenario_2_4
    def test_scenario_2_4(self, driver):
        """Test Scenario 2-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ2')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. The error message appears.
        apply_button.click()
        time.sleep(3)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_2")

    # pytest test_application_for_use.py::TestScenario2::test_scenario_2_5
    def test_scenario_2_5(self, driver):
        """Test Scenario 2-5
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ2')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. The error message appears.
        apply_button.click()
        time.sleep(3)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_2")

    # pytest test_application_for_use.py::TestScenario2::test_scenario_2_6
    def test_scenario_2_6(self, driver):
        """Test Scenario 2-6
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.
        4. Not working before checking the box.
        5. Registered content is downloaded.
        6. No "Request for register Data Usage Report" email is sent to the applicant.
        7. The error message appears on 11th download.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, 'テストシナリオ2')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(3)
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        header = modal.find_element(By.XPATH, './/*[@id="exampleModalLongTitle"]')
        terms = modal.find_element(By.XPATH, './/*[@id="terms"]')
        assert header.text == 'Terms and Conditions'
        assert terms.text == '利用規約のみ\nGuest'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_2")

        # 3. The print dialog appears.
        print_button = modal.find_element(By.XPATH, './/*[@id="print-btn"]')
        print_button.click()
        time.sleep(3)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_3")
        # reload page for close print dialog
        driver.switch_to.window(window_handles[0])
        time.sleep(3)
        driver.refresh()
        time.sleep(3)

        # 4. Not working before checking the box.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        apply_button.click()
        time.sleep(3)
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert not 'test_scenario_2.txt' in file_list

        # 5. Registered content is downloaded.
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(3)
        next_btn.click()
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_2.txt' in file_list

        # 6. No "Request for register Data Usage Report" email is sent to the applicant.
        assert check_mail(config.users['General']['mail'], 'テストシナリオ2')

        # 7. The error message appears on 11th download.
        for i in range(10):
            apply_button.click()
            time.sleep(3)
            modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
            modal_id = modal.get_attribute('id')
            next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
            next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
            check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
            check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
            if not check_box.is_selected():
                check_box.click()
                time.sleep(3)
            next_btn.click()
            time.sleep(3)
            if i < 9:
                file_list = os.listdir(config.base_download_dir)
                assert 'test_scenario_2 (' + str(i + 1) + ').txt' in file_list
            else:
                file_list = os.listdir(config.base_download_dir)
                assert 'test_scenario_2 (' + str(i + 1) + ').txt' not in file_list

        # delete downloaded files to do other tests
        delete_target_files = [file for file in file_list if file.startswith('test_scenario_2')]
        for file in delete_target_files:
            os.remove(config.base_download_dir + '/' + file)

# pytest test_application_for_use.py::TestScenario5
class TestScenario5:
    """Test Scenario 5
    
    Requirements for item to be used
        - The Providing Method is Usage Application
        - The Providing Role is General
        - The Terms and Conditions are voluntary
    """
    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_1
    def test_scenario_5_1(self, driver):
        """Test Scenario 5-1
        
        1. The Download button appears.
        2. Registered content is downloaded.
        3. No "Request for register Data Usage Report" email is sent to the applicant.
        
        User's role is Contributor and the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(driver, 'RegCon')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name + "_1")

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_5.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert check_mail(config.users['RegCon']['mail'], 'テストシナリオ5')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_5.txt')

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

def check_mail(mail_address, target_item_name):
    """Check the latest email
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
    """
    # get the latest email
    mail_list = os.listdir('mail/root/new')
    with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    # get the email title
    is_subject = False
    sub_list = []
    for line in lines:
        if line.startswith('Subject: ') and line.find('Undelivered') == -1:
            sub_list.append(line)
            is_subject = True
            continue
        if is_subject:
            if line.startswith('From: '):
                is_subject = False
                continue
            sub_list.append(line)

    # decode and check the email title
    decode_sub_list = []
    for sub in sub_list:
        decode_sub_list.append(decode_mail_subject(sub))
    if str.join('', decode_sub_list) == '利用報告の登録のお願い／Request for register Data Usage Report':
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')]
        if recipient[1].split(' ')[1] == mail_address:
            # check the email body
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            usage_data = [line for line in lines if line.startswith('利用データ：')]
            download_date = [line for line in lines if line.startswith('データダウンロード日：')]
            if len(body_mail_address) != 0\
                and body_mail_address[0].split('：')[1] == mail_address\
                and len(usage_data) != 0\
                and usage_data[0].split('：')[1] == target_item_name\
                and len(download_date) != 0\
                and download_date[0].split('：')[1]\
                    == datetime.datetime.today().strftime('%Y-%m-%d'):
                return False
    return True

def decode_mail_subject(param):
    """Decode the email subject
    
    Args:
        param(str): email subject"""
    if param.startswith('Subject: '):
        param_f = param.split(' ')[1]
    else:
        param_f = param.strip()

    str_list=[]
    if param_f.startswith('=?utf-8?b?'):
        str_list = param_f[10:].split('?=')
        str_list[0] = base64.b64decode(str_list[0]).decode('utf-8')
    elif param_f.startswith('=?utf-8?q?'):
        str_list = param_f[10:].split('?=')
        str_list[0] = quopri.decodestring(str_list[0]).decode('utf-8')
    else:
        str_list.append(param_f)
    return str.join('', str_list)

def check_login_page(driver):
    """Check transition destination is login page
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # check transition destination is login page
    url = driver.current_url
    assert url.startswith(config.base_url + '/login'), 'Transition destination is not login page'

    # check next page is record page
    url_next = url.split('?next=')[1]
    assert url_next.find('record') != -1, 'Next page is not record page'

def save_screenshot(driver, co_name):
    """Save screenshot
    
    Args:
        driver(WebDriver): WebDriver object
        co_name(str): test case name
    """
    time.sleep(3)
    driver.save_screenshot(
        config.base_save_folder + 'application_for_use/' + d + "_" + co_name + ".png")
