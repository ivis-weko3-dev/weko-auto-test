import inspect
import os
import subprocess

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_1.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['RegCon']['mail'], 'テストシナリオ1')

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_1.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['PrxRegCon']['mail'], 'テストシナリオ1')

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario1::test_scenario_1_5_1_to_3
    def test_scenario_1_5_1_to_3(self, driver):
        """Test Scenario 1-5-1, 1-5-2, 1-5-3
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        header = modal.find_element(By.XPATH, './/*[@id="exampleModalLongTitle"]')
        terms = modal.find_element(By.XPATH, './/*[@id="terms"]')
        assert header.text == 'Terms and Conditions'
        assert terms.text == '利用規約のみ\nGeneral'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

        # 3. The print dialog appears.
        print_button = modal.find_element(By.XPATH, './/*[@id="print-btn"]')
        print_button.click()
        time.sleep(1)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '3')
        driver.switch_to.window(window_handles[0])
        time.sleep(1)

    # pytest test_application_for_use.py::TestScenario1::test_scenario_1_5_4
    def test_scenario_1_5_4(self, driver):
        """Test Scenario 1-5-4
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        4. Not working before checking the box.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ1')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 4. Not working before checking the box.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert not 'test_scenario_1.txt' in file_list

    # pytest test_application_for_use.py::TestScenario1::test_scenario_1_5_5_and_6
    def test_scenario_1_5_5_and_6(self, driver):
        """Test Scenario 1-5-5, 1-5-6
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
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
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 5. Registered content is downloaded.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_1.txt' in file_list

        # 6. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['General']['mail'], 'テストシナリオ1')

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_2.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['RegCon']['mail'], 'テストシナリオ2')

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_2.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['PrxRegCon']['mail'], 'テストシナリオ2')

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario2::test_scenario_2_6_1_to_3
    def test_scenario_2_6_1_to_3(self, driver):
        """Test Scenario 2-6-1, 2-6-2, 2-6-3
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.
        
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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        header = modal.find_element(By.XPATH, './/*[@id="exampleModalLongTitle"]')
        terms = modal.find_element(By.XPATH, './/*[@id="terms"]')
        assert header.text == 'Terms and Conditions'
        assert terms.text == '利用規約のみ\nGuest'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

        # 3. The print dialog appears.
        print_button = modal.find_element(By.XPATH, './/*[@id="print-btn"]')
        print_button.click()
        time.sleep(1)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(1)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '3')
        driver.switch_to.window(window_handles[0])
        time.sleep(1)

    # pytest test_application_for_use.py::TestScenario2::test_scenario_2_6_4
    def test_scenario_2_6_4(self, driver):
        """Test Scenario 2-6-4
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        4. Not working before checking the box.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, 'テストシナリオ2')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 4. Not working before checking the box.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert not 'test_scenario_2.txt' in file_list

    # pytest test_application_for_use.py::TestScenario2::test_scenario_2_6_5_to_7
    def test_scenario_2_6_5_to_7(self, driver):
        """Test Scenario 2-6-5, 2-6-6, 2-6-7
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
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
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 5. Registered content is downloaded.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_2.txt' in file_list

        # 6. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['General']['mail'], 'テストシナリオ2')

        # 7. The error message appears on 11th download.
        for i in range(10):
            apply_button.click()
            time.sleep(1)
            modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
            modal_id = modal.get_attribute('id')
            next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
            next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
            check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
            check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
            if not check_box.is_selected():
                check_box.click()
                time.sleep(1)
            next_btn.click()
            time.sleep(1)
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

# pytest test_application_for_use.py::TestScenario3
class TestScenario3:
    """Test Scenario 3
    
    Requirements for item to be used
        - The Providing Method is Usage Registration
        - The Providing Role is General
        - The Terms and Conditions are voluntary
    """
    # pytest test_application_for_use.py::TestScenario3::test_scenario_3_1
    def test_scenario_3_1(self, driver):
        """Test Scenario 3-1
        
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
        search_and_display_target_item(driver, 'テストシナリオ3')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_3.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['RegCon']['mail'], 'テストシナリオ3')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_3.txt')

    # pytest test_application_for_use.py::TestScenario3::test_scenario_3_2
    def test_scenario_3_2(self, driver):
        """Test Scenario 3-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ3')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario3::test_scenario_3_3
    def test_scenario_3_3(self, driver):
        """Test Scenario 3-3
        
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
        search_and_display_target_item(driver, 'テストシナリオ3')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_3.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['PrxRegCon']['mail'], 'テストシナリオ3')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_3.txt')

    # pytest test_application_for_use.py::TestScenario3::test_scenario_3_4
    def test_scenario_3_4(self, driver):
        """Test Scenario 3-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ3')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario3::test_scenario_3_5
    def test_scenario_3_5(self, driver):
        """Test Scenario 3-5
        
        This test is not implemented.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        assert False, 'The test of Scenario 3-5 is not implemented.'

    # pytest test_application_for_use.py::TestScenario3::test_scenario_3_6
    def test_scenario_3_6(self, driver):
        """Test Scenario 3-6
        
        1. Transition to the login page
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # 1. Transition to the login page
        search_and_display_target_item(driver, 'テストシナリオ3')
        check_login_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

# pytest test_application_for_use.py::TestScenario4
class TestScenario4:
    """Test Scenario 4
    
    Requirements for item to be used
        - The Providing Method is Usage Registration
        - The Providing Role is Guest
        - The Terms and Conditions are voluntary
    """
    # pytest test_application_for_use.py::TestScenario4::test_scenario_4_1
    def test_scenario_4_1(self, driver):
        """Test Scenario 4-1
        
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
        search_and_display_target_item(driver, 'テストシナリオ4')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_4.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['RegCon']['mail'], 'テストシナリオ4')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_4.txt')

    # pytest test_application_for_use.py::TestScenario4::test_scenario_4_2
    def test_scenario_4_2(self, driver):
        """Test Scenario 4-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ4')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario4::test_scenario_4_3
    def test_scenario_4_3(self, driver):
        """Test Scenario 4-3
        
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
        search_and_display_target_item(driver, 'テストシナリオ4')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_4.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['PrxRegCon']['mail'], 'テストシナリオ4')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_4.txt')

    # pytest test_application_for_use.py::TestScenario4::test_scenario_4_4
    def test_scenario_4_4(self, driver):
        """Test Scenario 4-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ4')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario4::test_scenario_4_5
    def test_scenario_4_5(self, driver):
        """Test Scenario 4-5
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ4')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario4::test_scenario_4_6
    def test_scenario_4_6(self, driver):
        """Test Scenario 4-6
        
        This test is not implemented.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        assert False, 'The test of Scenario 4-6 is not implemented.'

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
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_5.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['RegCon']['mail'], 'テストシナリオ5')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_5.txt')

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_2
    def test_scenario_5_2(self, driver):
        """Test Scenario 5-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_3
    def test_scenario_5_3(self, driver):
        """Test Scenario 5-3
        
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
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_5.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['PrxRegCon']['mail'], 'テストシナリオ5')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_5.txt')

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_4
    def test_scenario_5_4(self, driver):
        """Test Scenario 5-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Apply button appears.
        save_screenshot(driver, inspect.currentframe().f_code.co_name, 'test')
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_5_1_to_3
    def test_scenario_5_5_1_to_3(self, driver):
        """Test Scenario 5-5-1, 5-5-2, 5-5-3
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Apply button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        header = modal.find_element(By.XPATH, './/*[@id="exampleModalLongTitle"]')
        terms = modal.find_element(By.XPATH, './/*[@id="terms"]')
        assert header.text == 'Terms and Conditions'
        assert terms.text == '利用申請\nGeneral'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

        # 3. The print dialog appears.
        print_button = modal.find_element(By.XPATH, './/*[@id="print-btn"]')
        print_button.click()
        time.sleep(1)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '3')
        driver.switch_to.window(window_handles[0])
        time.sleep(1)

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_5_4
    def test_scenario_5_5_4(self, driver):
        """Test Scenario 5-5-4
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        4. Not working before checking the box.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 4. Not working before checking the box.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(1)
        assert not driver.current_url.startswith(config.base_url + '/workflow/activity/detail')

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_5_5_and_6_and_10_to_13
    def test_scenario_5_5_5_and_6_and_10_to_13(self, driver):
        """Test Scenario 5-5-5, 5-5-6, 5-5-10, 5-5-11, 5-5-12, 5-5-13
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        6. A reminder email is sent to the applicant.
        10. The usage application workflow with the action status "Approval" is displayed.
        11. The Download button appears and the registered content is downloaded.
        12. "Request for register Data Usage Report" email is sent to the applicant.
        13. "Your Application was Received" email is sent to the applicant.

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 5. Transition to the usage application workflow.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '5')

        # 6. A reminder email is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '6')
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert check_request_for_approval_mail(
            config.users['General']['mail'],
            'テストシナリオ5',
            activity_id)

        # 10. The usage application workflow with the action status "Approval" is displayed.
        logout(driver)
        login(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        # action_idx = headers_text.index('Action')
        status_idx = headers_text.index('Status')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        target_element = None
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                # assert rds[action_idx - 1].text == 'Approval'
                assert rds[status_idx - 1].text == 'Approval'
                target_element = rds[activity_id_idx - 1]
                break
        assert target_element, 'Could not get target workflow'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '10')

        # 11. The Download button appears and the registered content is downloaded.
        target_element.find_element(By.TAG_NAME, 'a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-approval"]').click()
        time.sleep(3)
        logout(driver)
        login(driver, 'General')
        search_and_display_target_item(driver, 'テストシナリオ5')
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '11')
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_5.txt' in file_list

        # 12 and 13 are not created because the mail cannot be checked

        # download the file 9 times to do other tests
        search_and_display_target_item(driver, 'テストシナリオ5')
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        for _ in range(9):
            download_button.click()
            time.sleep(1)

        # delete downloaded files to do other tests
        file_list = os.listdir(config.base_download_dir)
        delete_target_files = [file for file in file_list if file.startswith('test_scenario_5')]
        for file in delete_target_files:
            os.remove(config.base_download_dir + '/' + file)

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_5_8
    def test_scenario_5_5_8(self, driver):
        """Test Scenario 5-5-8
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        8. Transition to the workflow with input retained.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 5. Transition to the usage application workflow.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)

        # 8. Transition to the workflow with input retained.
        # edit target is Research Title
        before_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        research_title = 'test research'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_research_title"]')\
            .send_keys(research_title)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '8_before')
        driver.find_elements(By.CLASS_NAME, 'save-button')[1].click()
        time.sleep(3)
        # press the Apply button again to check the input is retained
        search_and_display_target_item(driver, 'テストシナリオ5')
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')
        apply_button.click()
        time.sleep(1)
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)
        after_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert before_activity_id == after_activity_id
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_research_title"]')
        assert target_element.get_attribute('value') == research_title
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '8_after')

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_5_9
    def test_scenario_5_5_9(self, driver):
        """Test Scenario 5-5-9
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        9. Transition to the new usage application workflow.

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 5. Transition to the usage application workflow.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)

        # 9. Transition to the new usage application workflow.
        # edit target is Research Title
        before_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        research_title = 'test research'
        driver.find_element(By.XPATH, '//*[@id="subitem_restricted_access_research_title"]')\
            .send_keys(research_title)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '9_before')
        driver.find_element(By.XPATH, '//*[@id="btn_quit"]').click()
        time.sleep(3)
        # press the Apply button again to check the input is retained
        search_and_display_target_item(driver, 'テストシナリオ5')
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')
        apply_button.click()
        time.sleep(1)
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)
        after_activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert before_activity_id != after_activity_id
        panel_toggles = driver.find_elements(By.CLASS_NAME, 'panel-toggle')
        for pt in panel_toggles:
            if pt.text == 'Research Title':
                research_title_location = pt.location
                driver.execute_script(
                    'window.scrollTo(0, ' + str(research_title_location['y'] - 100) + ')')
                pt.click()
                time.sleep(1)
                break
        target_element = driver.find_element(
            By.XPATH,
            '//*[@id="subitem_restricted_access_research_title"]')
        assert target_element.get_attribute('value') != research_title
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '9_after')

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_5_14
    def test_scenario_5_5_14(self, driver):
        """Test Scenario 5-5-14
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        6. A reminder email is sent to the applicant.
        11. The Download button appears and the registered content is downloaded.
        14. Transition to the workflow with input retained.

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 5. Transition to the usage application workflow.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)

        # 6. A reminder email is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text

        # 11. The Download button appears and the registered content is downloaded.
        logout(driver)
        login(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        driver.find_element(By.XPATH, '//*[@id="btn-approval"]').click()
        time.sleep(3)
        logout(driver)
        login(driver, 'General')
        search_and_display_target_item(driver, 'テストシナリオ5')
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        actions_td.find_elements(By.TAG_NAME, 'a')[0].click()
        time.sleep(1)

        # 14. Transition to the workflow with input retained.

        # download the file 9 times to do other tests
        search_and_display_target_item(driver, 'テストシナリオ5')
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        for _ in range(9):
            download_button.click()
            time.sleep(1)

        # delete downloaded files to do other tests
        file_list = os.listdir(config.base_download_dir)
        delete_target_files = [file for file in file_list if file.startswith('test_scenario_5')]
        for file in delete_target_files:
            os.remove(config.base_download_dir + '/' + file)

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_5_15
    def test_scenario_5_5_15(self, driver):
        """Test Scenario 5-5-15
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        6. A reminder email is sent to the applicant.
        11. The Download button appears and the registered content is downloaded.
        15. Status is recorded in the workflow tab as aborted.

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 5. Transition to the usage application workflow.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)

        # 6. A reminder email is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text

        # 11. The Download button appears and the registered content is downloaded.
        logout(driver)
        login(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        driver.find_element(By.XPATH, '//*[@id="btn-approval"]').click()
        time.sleep(3)
        logout(driver)
        login(driver, 'General')
        search_and_display_target_item(driver, 'テストシナリオ5')
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        actions_td.find_elements(By.TAG_NAME, 'a')[0].click()
        time.sleep(1)

        # 15. Status is recorded in the workflow tab as aborted.

        # download the file 9 times to do other tests
        search_and_display_target_item(driver, 'テストシナリオ5')
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        for _ in range(9):
            download_button.click()
            time.sleep(1)

        # delete downloaded files to do other tests
        file_list = os.listdir(config.base_download_dir)
        delete_target_files = [file for file in file_list if file.startswith('test_scenario_5')]
        for file in delete_target_files:
            os.remove(config.base_download_dir + '/' + file)

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_5_16
    def test_scenario_5_5_16(self, driver):
        """Test Scenario 5-5-16
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. Transition to the usage application workflow.
        6. A reminder email is sent to the applicant.
        16. An approval rejection email is sent to the applicant.
            The status of the action of the usage application changed back to "Item Registration".

        User's role is General

        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ5')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 5. Transition to the usage application workflow.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(3)

        # 6. A reminder email is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text

        # 16. An approval rejection email is sent to the applicant.
        #     The status of the action of the usage application changed back to "Item Registration".
        logout(driver)
        login(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(1)
                break
        driver.find_element(By.XPATH, '//*[@id="btn-reject"]').click()
        time.sleep(3)
        logout(driver)
        login(driver, 'General')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        # action_idx = headers_text.index('Action')
        status_idx = headers_text.index('Status')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                # assert rds[action_idx - 1].text == 'Item Registration'
                assert rds[status_idx - 1].text == 'Item Registration'
                break
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '16')
        assert check_results_of_the_review_mail(
            config.users['General']['mail'],
            'テストシナリオ5',
            activity_id)

    # pytest test_application_for_use.py::TestScenario5::test_scenario_5_6
    def test_scenario_5_6(self, driver):
        """Test Scenario 5-6
        
        1. Transition to the login page.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # 1. Transition to the login page.
        search_and_display_target_item(driver, 'テストシナリオ5')
        check_login_page(driver)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

# pytest test_application_for_use.py::TestScenario6
class TestScenario6:
    """Test Scenario 6
    
    Requirements for item to be used
        - The Providing Method is Usage Application
        - The Providing Role is Guest
        - The Terms and Conditions are voluntary
    """
    # pytest test_application_for_use.py::TestScenario6::test_scenario_6_1
    def test_scenario_6_1(self, driver):
        """ Test Scenario 6-1
        
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
        search_and_display_target_item(driver, 'テストシナリオ6')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_6.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['RegCon']['mail'], 'テストシナリオ6')

        # delete downloaded file to to other tests
        os.remove(config.base_download_dir + '/test_scenario_6.txt')

    # pytest test_application_for_use.py::TestScenario6::test_scenario_6_2
    def test_scenario_6_2(self, driver):
        """ Test Scenario 6-2
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Contributor and not the item's owner
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Contributor
        login(driver, 'NoRegCon')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ6')

        # 1. The Apply button appears.
        action_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = action_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario6::test_scenario_6_3
    def test_scenario_6_3(self, driver):
        """Test Scenario 6-3
        
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
        search_and_display_target_item(driver, 'テストシナリオ6')

        # 1. The Download button appears.
        actions_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        download_button = actions_td.find_elements(By.TAG_NAME, 'a')[0]
        assert download_button.text == 'Download'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. Registered content is downloaded.
        download_button.click()
        time.sleep(1)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_6.txt' in file_list

        # 3. No "Request for register Data Usage Report" email is sent to the applicant.
        assert not check_request_for_register_mail(config.users['PrxRegCon']['mail'], 'テストシナリオ6')

        # delete downloaded file to to other tests
        os.remove(config.base_download_dir + '/test_scenario_6.txt')

    # pytest test_application_for_use.py::TestScenario6::test_scenario_6_4
    def test_scenario_6_4(self, driver):
        """Test Scenario 6-4
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is Community Administrator
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as Community Administrator
        login(driver, 'Community')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ6')

        # 1. The Apply button appears.
        action_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = action_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario6::test_scenario_6_5
    def test_scenario_6_5(self, driver):
        """Test Scenario 6-5
        
        1. The Apply button appears.
        2. The error message appears.
        
        User's role is General
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # log in as General
        login(driver, 'General')

        # search target item
        search_and_display_target_item(driver, 'テストシナリオ6')

        # 1. The Apply button appears.
        action_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = action_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The error message appears.
        apply_button.click()
        time.sleep(1)
        modals = driver.find_elements(By.XPATH, '//*[@id="allModal"]')
        assert len(modals) == 1
        err_msg = driver.find_element(By.XPATH, '//*[@id="inputModal"]')
        assert err_msg.text == config.application_for_use_error_msg
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

    # pytest test_application_for_use.py::TestScenario6::test_scenario_6_6_1_to_3
    def test_scenario_6_6_1_to_3(self, driver):
        """Test Scenario 6-6-1, 6-6-2, 6-6-3
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        3. The print dialog appears.
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, 'テストシナリオ6')

        # 1. The Apply button appears.
        action_td = driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]')
        apply_button = action_td.find_elements(By.TAG_NAME, 'a')[0]
        assert apply_button.text == 'Apply'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '1')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        header = modal.find_element(By.XPATH, './/*[@id="exampleModalLongTitle"]')
        terms = modal.find_element(By.XPATH, './/*[@id="terms"]')
        assert header.text == 'Terms and Conditions'
        assert terms.text == '利用申請\nGuest'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '2')

        # 3. The print dialog appears.
        print_button = modal.find_element(By.XPATH, './/*[@id="print-btn"]')
        print_button.click()
        time.sleep(1)
        window_handles = driver.window_handles
        # after print button clicked, window handles increase
        assert len(window_handles) == 2
        driver.switch_to.window(window_handles[1])
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '3')
        driver.switch_to.window(window_handles[0])
        time.sleep(1)

    # pytest test_application_for_use.py::TestScenario6::test_scenario_6_6_4
    def test_scenario_6_6_4(self, driver):
        """Test Scenario 6-6-4
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        4. Not working before checking the box
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, 'テストシナリオ6')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 4. Not working before checking the box
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        next_btn.click()
        time.sleep(1)
        assert not driver.current_url.startswith(config.base_url + '/workflow/activity/detail')

    # pytest test_application_for_use.py::TestScenario6::test_scenario_6_6_5_to_7_and_19
    def test_scenario_6_6_5_to_7_and_19(self, driver):
        """Test Scenario 6-6-5, 6-6-6, 6-6-7, 6-6-19
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. Transition to the workflow page.
        7. A mail acknowledging receipt of the usage application is sent to the applicant.
        19. An approval rejection email is sent to the applicant.
            The status of the action of the usage application changed back to "Item Registration".
        
        User is not logged in
        
        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, 'テストシナリオ6')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 5. The account entry dialog appears.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '5')

        # 6. Transition to the workflow page.
        A14(driver, config.guest_mail)
        mail_list = os.listdir('mail/root/new')
        with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        applicant_address = [line for line in lines if line.startswith('To: ')][1].split(' ')[1]
        assert applicant_address == config.guest_mail
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '6')

        # 7. A mail acknowledging receipt of the usage application is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '7')
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert check_request_for_approval_mail_for_guest(config.guest_mail, 'テストシナリオ6', activity_id)

        # 19. An approval rejection email is sent to the applicant.
        #     The status of the action of the usage application changed back to "Item Registration".
        login(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break
        driver.find_element(By.XPATH, '//*[@id="btn-reject"]').click()
        time.sleep(3)
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        # action_idx = headers_text.index('Action')
        status_idx = headers_text.index('Status')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                # assert rds[action_idx - 1].text == 'Item Registration'
                assert rds[status_idx - 1].text == 'Item Registration'
                break
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '19')
        assert check_results_of_the_review_mail_for_guest(
            config.guest_mail,
            'テストシナリオ6',
            activity_id)

        # cancel the workflow to do other tests
        logout(driver)
        driver.get(url)
        time.sleep(3)
        A20(driver)
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

    # pytest test_application_for_use.py::TestScenario6::test_scenario_6_6_11_to_16
    def test_scenario_6_6_11_to_16(self, driver):
        """Test Scenario 6-6-11, 6-6-12, 6-6-13, 6-6-14, 6-6-15, 6-6-16
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. Transition to the workflow page.
        7. A mail acknowledging receipt of the usage application is sent to the applicant.
        11. The usage application workflow with the action status "Approval" is displayed.
        12. An approval notification email is sent to the applicant.
        13. The error message appears.
        14. Registered content is downloaded.
        15. "Request for register Data Usage Report" email is sent to the applicant.
        16. "Your Application was Received" email is sent to the applicant.

        User is not logged in

        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, 'テストシナリオ6')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 5. The account entry dialog appears.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)

        # 6. Transition to the workflow page.
        A14(driver, config.guest_mail)
        mail_list = os.listdir('mail/root/new')
        with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 7. A mail acknowledging receipt of the usage application is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text

        # 11. The usage application workflow with the action status "Approval" is displayed.
        login(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        # action_idx = headers_text.index('Action')
        status_idx = headers_text.index('Status')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        target_element = None
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                # assert rds[action_idx - 1].text == 'Approval'
                assert rds[status_idx - 1].text == 'Approval'
                target_element = rds[activity_id_idx - 1]
                break
        assert target_element, 'Could not get target workflow'
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '11')

        # 12. An approval notification email is sent to the applicant.
        target_element.find_element(By.TAG_NAME, 'a').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-approval"]').click()
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '12')
        assert check_approved_application_mail_for_guest(
            config.guest_mail,
            'テストシナリオ6',
            activity_id)

        # 13. The error message appears.
        logout(driver)
        mail_list = os.listdir('mail/root/new')
        with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        A18(driver, config.users['General']['mail'])
        time.sleep(1)
        alert = driver.switch_to.alert
        alert_msg = alert.text
        assert alert_msg == 'Could not download file.'
        alert.accept()
        # save_screenshot(driver, inspect.currentframe().f_code.co_name, '13')

        # 14. Registered content is downloaded.
        driver.get(url)
        time.sleep(3)
        A18(driver, config.guest_mail)
        time.sleep(3)
        file_list = os.listdir(config.base_download_dir)
        assert 'test_scenario_6.txt' in file_list

        # 15. "Request for register Data Usage Report" email is sent to the applicant.
        assert check_request_for_register_mail(config.guest_mail, 'テストシナリオ6', activity_id)

        # 16. "Your Application was Received" email is sent to the applicant.
        mail_list = os.listdir('mail/root/new')
        with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        assert check_received_application_mail(
            config.guest_mail,
            'テストシナリオ6',
            activity_id)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '16')

        # cancel the workflow to do other tests
        login(driver, 'Repository')
        driver.get(config.base_url + '/workflow/activity/detail/' + activity_id)
        time.sleep(3)
        A20(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_6.txt')

    # pytest test_application_for_use.py::TestScenario6::test_scenario_6_6_18
    def test_scenario_6_6_18(self, driver):
        """Test Scenario 6-6-18
        
        1. The Apply button appears.
        2. The Terms and Conditions modal appears.
        5. The account entry dialog appears.
        6. Transition to the workflow page.
        7. A mail acknowledging receipt of the usage application is sent to the applicant.
        11. The usage application workflow with the action status "Approval" is displayed.
        12. An approval notification email is sent to the applicant.
        14. Registered content is downloaded.
        18. The status of the target workflow is "Canceled"

        User is not logged in

        Args:
            driver(WebDriver): WebDriver object
        """
        # search target item
        search_and_display_target_item(driver, 'テストシナリオ6')

        # 1. The Apply button appears.
        apply_button = driver.find_element(
            By.XPATH,
            '//*[@id="detail-item"]/table/tbody/tr/td[3]/a')

        # 2. The Terms and Conditions modal appears.
        apply_button.click()
        time.sleep(1)

        # 5. The account entry dialog appears.
        modal = driver.find_element(By.CLASS_NAME, 'modal.fade.in')
        modal_id = modal.get_attribute('id')
        next_id = modal_id.replace('term_and_condtion_modal', 'term_next')
        next_btn = modal.find_element(By.XPATH, './/*[@id="' + next_id + '"]')
        check_id = modal_id.replace('term_and_condtion_modal', 'term_checked')
        check_box = modal.find_element(By.XPATH, './/*[@id="' + check_id + '"]')
        check_box.click()
        time.sleep(1)
        next_btn.click()
        time.sleep(1)

        # 6. Transition to the workflow page.
        A14(driver, config.guest_mail)
        mail_list = os.listdir('mail/root/new')
        with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)

        # 7. A mail acknowledging receipt of the usage application is sent to the applicant.
        driver.find_element(By.CLASS_NAME, 'next-button').click()
        time.sleep(3)
        driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
        time.sleep(3)
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text

        # 11. The usage application workflow with the action status "Approval" is displayed.
        login(driver, 'Repository')
        driver.get(config.base_url + '/workflow/')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                rds[activity_id_idx - 1].find_element(By.TAG_NAME, 'a').click()
                time.sleep(3)
                break

        # 12. An approval notification email is sent to the applicant.
        driver.find_element(By.XPATH, '//*[@id="btn-approval"]').click()
        time.sleep(3)

        # 14. Registered content is downloaded.
        logout(driver)
        mail_list = os.listdir('mail/root/new')
        with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        A18(driver, config.guest_mail)
        time.sleep(3)

        # 18. The status of the target workflow is "Canceled"
        mail_list = os.listdir('mail/root/new')
        with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        url = [line for line in lines if line.startswith('https://')][0]
        driver.get(url)
        time.sleep(3)
        save_screenshot(driver, inspect.currentframe().f_code.co_name, 'test')
        activity_id = driver.find_element(By.XPATH, '//*[@id="activity_id"]').text
        A20(driver)
        time.sleep(1)
        driver.find_element(By.XPATH, '//*[@id="btn_cancel"]').click()
        time.sleep(3)
        login(driver, 'Repository')
        driver.get(config.base_url + '/workflow/?tab=all')
        time.sleep(1)
        table = driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table')
        headers_text = [header.text for header in table.find_elements(By.TAG_NAME, 'th')]
        activity_id_idx = headers_text.index('Activity')
        # status_idx = headers_text.index('Status')
        user_idx = headers_text.index('User')
        rows = table.find_element(By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')
        for row in rows:
            # the tag of the first of row's cell is 'th', so idx - 1 is correct
            rds = row.find_elements(By.TAG_NAME, 'td')
            if rds[activity_id_idx - 1].text == activity_id:
                # assert rds[status_idx - 1].text == 'Canceled'
                assert rds[user_idx - 1].text == 'Canceled'
                break
        save_screenshot(driver, inspect.currentframe().f_code.co_name, '18')

        # delete downloaded file to do other tests
        os.remove(config.base_download_dir + '/test_scenario_6.txt')

def login(driver, target_key: str):
    """Log in as target user
    
    Args:
        driver(WebDriver): WebDriver object
        target_key(str): target user's key in config
    """
    # set login_user from config
    login_user = config.users[target_key]
    # log in as target user
    A1(driver, login_user['mail'], login_user['password'])

def check_request_for_register_mail(
        mail_address: str,
        target_item_name: str,
        activity_id: str = None):
    """Check the latest email

    for Request for register Data Usage Report
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest email
    mail_list = os.listdir('mail/root/new')
    with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == '利用報告の登録のお願い／Request for register Data Usage Report':
        print('subject')
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')]
        if recipient[1].split(' ')[1] == mail_address:
            print('recipient')
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            usage_data = [line for line in lines if line.startswith('申請データ：')]
            download_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, usage_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    download_date):
                print('three')
                if activity_id:
                    return compare_the_two_elements(activity_id, body_activity_id)
                return True
    return False

def check_request_for_approval_mail(mail_address: str, target_item_name: str, activity_id: str):
    """Check the latest email

    for Request for Approval of Application for Use
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    mail_list = os.listdir('mail/root/new')
    with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == '利用申請の承認のお願い／Request for Approval of Application for Use':
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')]
        if recipient[1].split(' ')[1] == config.users['Repository']['mail']:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_request_for_approval_mail_for_guest(
        mail_address: str,
        target_item_name: str,
        activity_id: str
    ):
    """Check the latest email
    
    for Request for Approval of Application for Use (for guest user)
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    mail_list = os.listdir('mail/root/new')
    with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list)\
        == 'データ利用申請の承認のお願い（ゲストユーザー向け）／Request for Approval of Application for Use  （for guest user）':
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')]
        if recipient[1].split(' ')[1] == config.users['Repository']['mail']:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_approved_application_mail_for_guest(
    mail_address: str,
    target_item_name: str,
    activity_id: str):
    """Check the latest email
    
    for Guest''s application was approved （for guest user）
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    mail_list = os.listdir('mail/root/new')
    with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list)\
        == '利用申請の承認のお知らせ（ゲストユーザー向け）／Guest\'\'s application was approved （for guest user）':
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')]
        if recipient[1].split(' ')[1] == mail_address:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_results_of_the_review_mail(mail_address: str, target_item_name: str, activity_id: str):
    """Check the latest email
    
    for The results of the review of your application
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    mail_list = os.listdir('mail/root/new')
    with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list)\
        == '利用申請の審査結果について／The results of the review of your application':
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')]
        if recipient[1].split(' ')[1] == mail_address:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_results_of_the_review_mail_for_guest(
        mail_address: str,
        target_item_name: str,
        activity_id: str):
    """Check the latest email
    
    for The results of the review of your application (for guest user)

    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    mail_list = os.listdir('mail/root/new')
    with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list)\
        == '利用申請の審査結果について（ゲストユーザー向け）／The results of the review of your application  （for guest user）':
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')]
        if recipient[1].split(' ')[1] == mail_address:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def check_received_application_mail(mail_address: str, target_item_name: str, activity_id: str):
    """Check the latest email
    
    for Your Application was Received
    
    Args:
        mail_address(str): recipient's email address
        target_item_name(str): target item's name
        activity_id(str): activity id
    """
    # get the latest mail
    mail_list = os.listdir('mail/root/new')
    with open('mail/root/new/' + mail_list[-1], 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()

    # get the email title
    sub_list = get_mail_subject(lines)

    # decode and check the email title
    if decode_mail_subject(sub_list) == '利用報告の受付のお知らせ／Your Application was Received':
        # check recipient's address
        recipient = [line for line in lines if line.startswith('To: ')]
        if recipient[1].split(' ')[1] == mail_address:
            # check the email body
            body_activity_id = [line for line in lines if line.startswith('申請番号：')]
            body_mail_address = [line for line in lines if line.startswith('メールアドレス：')]
            request_data = [line for line in lines if line.startswith('申請データ：')]
            request_date = [line for line in lines if line.startswith('申請年月日：')]
            if compare_the_two_elements(activity_id, body_activity_id)\
                and compare_the_two_elements(mail_address, body_mail_address)\
                and compare_the_two_elements(target_item_name, request_data)\
                and compare_the_two_elements(
                    datetime.datetime.today().strftime('%Y-%m-%d'),
                    request_date):
                return True
    return False

def get_mail_subject(lines: list[str]):
    """Get the email subject
    
    Args:
        lines(list[str]): email lines
    """
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
    return sub_list

def decode_mail_subject(param_list: list[str]):
    """Decode the email subject
    
    Args:
        param_list(list[str]): email subject"""
    plasticated_list = []
    for param in param_list:
        if param.startswith('Subject: '):
            plasticated_list.append(param.split(' ')[1])
        else:
            plasticated_list.append(param)

    echo_target = str.join('\n', plasticated_list)
    return subprocess.run(
        'echo "' + echo_target + '" | nkf -wd',
        capture_output=True,
        text=True,
        shell=True,
        check=True).stdout.replace('\n', '')

def compare_the_two_elements(expected: str, actual: list[str]):
    """Compare the two elements
    
    Args:
        expected(str): expected element
        actual(list[str]): actual element
    """
    return len(actual) > 0 and expected == actual[0].split('：')[1].strip()

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

def save_screenshot(driver, co_name: str, scenario_number: str):
    """Save screenshot
    
    Args:
        driver(WebDriver): WebDriver object
        co_name(str): test case name
        scenario_number(str): scenario number
    """
    idx = -1
    for _ in range(4):
        idx = co_name.find('_', idx + 1)
    if idx != -1:
        co_name = co_name[:idx]
    co_name = co_name + "_" + scenario_number
    time.sleep(1)
    driver.save_screenshot(
        config.base_save_folder + 'application_for_use/' + d + "_" + co_name + ".png")
