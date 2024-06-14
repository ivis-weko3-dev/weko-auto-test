import datetime
import inspect

import config
from methods_required_during_testing import *

def test_no_1(driver):
    """No.1 Secret URL button is hidden

    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Repository Administrator

    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # enable secret url, Expiration Date is 3, Download Limit is 3
    set_secret_url(driver, True)
    A3(driver, 3)
    A4(driver, 3)

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_2(driver):
    """No.2 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_3(driver):
    """No.3 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and not the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'NoRegCon')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_4(driver):
    """No.4 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and the item's contributor
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'PrxRegCon')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_5(driver):
    """No.5 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Community Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login(driver, 'Community')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_6(driver):
    """No.6 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User don't have any role
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as General
    login(driver, 'General')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_7(driver):
    """No.7 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User is not logged in

    Args:
        driver(WebDriver): WebDriver object
    """

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_8(driver):
    """No.8 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_9(driver):
    """No.9 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_10(driver):
    """No.10 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and not the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'NoRegCon')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_11(driver):
    """No.11 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and the item's contributor

    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'PrxRegCon')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_12(driver):
    """No.12 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Community Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login(driver, 'Community')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_13(driver):
    """No.13 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User don't have any role

    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as General
    login(driver, 'General')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_14(driver):
    """No.14 Transition to the login page
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User is not logged in
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check transition destination is login page
    check_login_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_15(driver):
    """No.15 Secret URL button is not hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is not hidden
    check_secret_url_button_is_hidden(driver, False)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

# No.16 - No.20 are not created because No.15 is failed

def test_no_21(driver):
    """No.21 Secret URL button is not hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is not hidden
    check_secret_url_button_is_hidden(driver, False)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

# No.22 - No.26 are not created because No.21 is failed

def test_no_27(driver):
    """No.27 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and not the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'NoRegCon')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_28(driver):
    """No.28 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's contributor
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'PrxRegCon')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_29(driver):
    """No.29 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Community Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login(driver, 'Community')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_30(driver):
    """No.30 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User don't have any role
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as General
    login(driver, 'General')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_31(driver):
    """No.31 Transition to the login page
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User is not logged in
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check transition destination is login page
    check_login_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_32(driver):
    """No.32 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_33(driver):
    """No.33 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_34(driver):
    """No.34 Secret URL button is hidden
    
    Secret URL is enabled
    Expliration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and not the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'NoRegCon')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_35(driver):
    """No.35 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and the item's contributor
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'PrxRegCon')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_36(driver):
    """No.36 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Community Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login(driver, 'Community')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_37(driver):
    """No.37 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User don't have any role
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as General
    login(driver, 'General')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_38(driver):
    """No.38 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User is not logged in
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_39(driver):
    """No.39 Secret URL button is not hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is not hidden
    check_secret_url_button_is_hidden(driver, False)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_40(driver):
    """No.40 Send email containing secret URL
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    A7(driver)

    # check mail
    check_secret_url_mail(driver, config.users['Repository']['mail'], 'B5_非公開', 3, 3)

def test_no_41(driver):
    """No.41 Download the target content
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # download the target content
    A8(driver, 'root')

    # check download file
    file_list = os.listdir(config.base_download_dir)
    assert 'private.txt' in file_list

def test_no_42(driver):
    """No.42 Try to download the target content over the download limit
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # download the target content several times
    # In No.41, download the content once, so the number of remaining downloads is 2
    for i in range(3):
        A8(driver, 'root')
        if i < 2:
            # check download file
            file_list = os.listdir(config.base_download_dir)
            assert 'private (' + str(i + 1) + ').txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

    # delete downloaded files to do other tests
    delete_target_files = [file for file in file_list if file.startswith('private')]
    for file in delete_target_files:
        os.remove(config.base_download_dir + '/' + file)

# No.43 is not created because this test is difficult to automate

def test_no_44(driver):
    """No.44 Secret URL different from No.40's secret URL
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    A7(driver)

    # check secret url
    check_secret_url_is_difference()

def test_no_45(driver):
    """No.45 Secret URL button is not hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is not hidden
    check_secret_url_button_is_hidden(driver, False)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_46(driver):
    """No.46 Send email containing secret URL
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    A7(driver)

    # check mail
    check_secret_url_mail(driver, config.users['RegCon']['mail'], 'B5_非公開', 3, 3)

def test_no_47(driver):
    """No.47 Download the target content
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # download the target content
    A8(driver, 'root')

    # check download file
    file_list = os.listdir(config.base_download_dir)
    assert 'private.txt' in file_list

def test_no_48(driver):
    """No.48 Try to download the target content over the download limit
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # download the target content several times
    # In No.47, download the content once, so the number of remaining downloads is 2
    for i in range(3):
        A8(driver, 'root')
        if i < 2:
            # check download file
            file_list = os.listdir(config.base_download_dir)
            assert 'private (' + str(i + 1) + ').txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

    # delete downloaded files to do other tests
    delete_target_files = [file for file in file_list if file.startswith('private')]
    for file in delete_target_files:
        os.remove(config.base_download_dir + '/' + file)

# No.49 is not created because this test is difficult to automate

def test_no_50(driver):
    """No.50 Secret URL different from No.46's secret URL
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    A7(driver)

    # check secret url
    check_secret_url_is_difference()

def test_no_51(driver):
    """No.51 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and not the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'NoRegCon')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_52(driver):
    """No.52 Secret URL button is hidden
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's contributor
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'PrxRegCon')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_53(driver):
    """No.53 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Community Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login(driver, 'Community')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_54(driver):
    """No.54 Display error message
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User don't have any role
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as General
    login(driver, 'General')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_55(driver):
    """No.55 Transition to the login page
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User is not logged in
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check transition destination is login page
    check_login_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_56(driver):
    """No.56 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # disable secret url
    set_secret_url(driver, False)

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_57(driver):
    """No.57 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_58(driver):
    """No.58 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and not the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'NoRegCon')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_59(driver):
    """No.59 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Contributor and the item's contributor
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'PrxRegCon')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_60(driver):
    """No.60 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User's Role is Community Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login(driver, 'Community')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_61(driver):
    """No.61 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User don't have any role
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as General
    login(driver, 'General')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_62(driver):
    """No.62 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Access
    User is not logged in
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_63(driver):
    """No.63 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_64(driver):
    """No.64 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_65(driver):
    """No.65 Display error message
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and not the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'NoRegCon')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_66(driver):
    """No.66 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Contributor and the item's contributor
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'PrxRegCon')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_67(driver):
    """No.67 Display error message
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User's Role is Community Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login(driver, 'Community')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_68(driver):
    """No.68 Display error message
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User don't have any role
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as General
    login(driver, 'General')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_69(driver):
    """No.69 Transition to the login page
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Restricted Access
    User is not logged in
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check transition destination is login page
    check_login_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_70(driver):
    """No.70 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_71(driver):
    """No.71 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_72(driver):
    """No.72 Display error message
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and not the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'NoRegCon')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_73(driver):
    """No.73 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Contributor and the item's contributor
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'PrxRegCon')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_74(driver):
    """No.74 Display error message
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User's Role is Community Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login(driver, 'Community')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_75(driver):
    """No.75 Display error message
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User don't have any role
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as General
    login(driver, 'General')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check permission error page
    check_permission_error_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_76(driver):
    """No.76 Transition to the login page
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is after today
    User is not logged in
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check transition destination is login page
    check_login_page(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_77(driver):
    """No.77 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_78(driver):
    """No.78 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_79(driver):
    """No.79 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and not the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'NoRegCon')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_80(driver):
    """No.80 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Contributor and the item's contributor
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'PrxRegCon')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_81(driver):
    """No.81 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User's Role is Community Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login(driver, 'Community')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_82(driver):
    """No.82 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User don't have any role
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as General
    login(driver, 'General')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_83(driver):
    """No.83 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Open Date and publish date is before today
    User is not logged in
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_84(driver):
    """No.84 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_85(driver):
    """No.85 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_86(driver):
    """No.86 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and not the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'NoRegCon')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_87(driver):
    """No.87 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's contributor
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Contributor
    login(driver, 'PrxRegCon')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_88(driver):
    """No.88 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Community Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Community Administrator
    login(driver, 'Community')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_89(driver):
    """No.89 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User don't have any role
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as General
    login(driver, 'General')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

def test_no_90(driver):
    """No.90 Secret URL button is hidden
    
    Secret URL is disabled
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User is not logged in
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

# No.91 is not created because No.15 is failed

# No.92 is not created because No.21 is failed

def test_no_93(driver):
    """No.93 Download file with secret URL is failed
    
    Secret URL is enabled and switch to disabled after email is sent
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Admministrator
    login(driver, 'Repository')

    # enable secret url
    set_secret_url(driver, True)

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    A7(driver)

    # disable secret url
    set_secret_url(driver, False)

    # download the target file
    A8(driver, 'root')

    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

def test_no_94(driver):
    """No.94 Download file with secret URL is failed
    
    Secret URL is enabled and switch to disabled after email is sent
    Expiration Date is 3
    Download Limit is 3
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator for enable secret url
    login(driver, 'Repository')

    # enable secret url
    set_secret_url(driver, True)

    # log out
    logout(driver)

    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    A7(driver)

    # log out
    logout(driver)

    # log in as Repository Administrator for disable secret url
    login(driver, 'Repository')

    # disable secret url
    set_secret_url(driver, False)

    # download the target file
    A8(driver, 'root')

    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

# No.95 is not created because No.15 is failed

# No.96 is not created because No.21 is failed

def test_no_97(driver):
    """No.97 The number of possible downloads changes by changing Download Limit
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3 and switch to 5 after email is sent
    Access Setting is Private
    User's Role is Repository Administrator
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator
    login(driver, 'Repository')

    # enable secret url and set download limit to 3
    set_secret_url(driver, True)
    A4(driver, 3)

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    A7(driver)

    # set download limit to 5
    A4(driver, 5)

    # download the target content several times
    for i in range(6):
        A8(driver, 'root')
        if i < 5:
            # check download file
            parentheses = ' (' + str(i) + ')' if i > 0 else ''
            file_list = os.listdir(config.base_download_dir)
            assert 'private' + parentheses + '.txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

    # delete download files to do other tests
    delete_target_files = [file for file in file_list if file.startswith('private')]
    for file in delete_target_files:
        os.remove(config.base_download_dir + '/' + file)

def test_no_98(driver):
    """No.98 The number of possible downloads changes by changing Download Limit
    
    Secret URL is enabled
    Expiration Date is 3
    Download Limit is 3 and switch to 5 after email is sent
    Access Setting is Private
    User's Role is Contributor and the item's owner
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # log in as Repository Administrator for set download limit to 3
    login(driver, 'Repository')

    # enable secret url and set download limit to 3
    set_secret_url(driver, True)
    A4(driver, 3)

    # log out
    logout(driver)

    # log in as Contributor
    login(driver, 'RegCon')

    # search target item
    search_and_display_target_item(driver, 'B5_非公開')

    # display content's info
    click_file_information_button(driver)

    # click secret url button
    A7(driver)

    # log out
    logout(driver)

    # log in as Repository Administrator for set download limit to 5
    login(driver, 'Repository')

    # set download limit to 5
    A4(driver, 5)

    # download the target content several times
    for i in range(6):
        A8(driver, 'root')
        if i < 5:
            # check download file
            parentheses = ' (' + str(i) + ')' if i > 0 else ''
            file_list = os.listdir(config.base_download_dir)
            assert 'private' + parentheses + '.txt' in file_list
        else:
            # check over download limit error message
            check_over_download_limit_error_message(driver)

    save_screenshot(driver, inspect.currentframe().f_code.co_name)

    # delete download files to do other tests
    delete_target_files = [file for file in file_list if file.startswith('private')]
    for file in delete_target_files:
        os.remove(config.base_download_dir + '/' + file)

# No.99-102 is no created because these tests are difficult to automate

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


def check_secret_url_button_is_hidden(driver, is_hidden):
    """Check secret url button is hidden or not
    
    Args:
        driver(WebDriver): WebDriver object
        is_hidden(bool): whether secret url button is hidden or not
    """
    # check secret url button is hidden or not
    table = driver.find_element(
        By.XPATH, '//*[@id="detail-item"]/div[3]/div/div[2]/div/div/div[1]/table')
    bodys = table.find_elements(By.XPATH, './/tbody/tr/td')
    is_exist = False
    for b in bodys:
        a_tag = b.find_elements(By.XPATH, './/a')
        for a in a_tag:
            if a.text == 'Secret URL':
                is_exist = True
                break
        if is_exist:
            break

    # is_hidden is True and is_exist is True -> assert False
    if is_hidden and is_exist:
        assert False, 'Secret URL button is not hidden'
    # is_hidden is False and is_exist is False -> assert False
    if not is_hidden and not is_exist:
        assert False, 'Secret URL button is hidden'
    assert True

def check_permission_error_page(driver):
    """Check permission error page
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # check error page does't have weko's panel component
    components = driver.find_elements(By.XPATH, '//*[@id="panel-main-content"]')
    assert len(components) == 0, 'This page is not error page'

    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

    # check error message
    error_message = error_page[0].find_element(By.XPATH, './/div/div/h1')
    assert error_message.text == 'Permission required', 'Error message is not "Permission required"'

def check_over_download_limit_error_message(driver):
    """Check over download limit error message
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

    # check error message
    error_message = error_page[0].find_element(By.XPATH, './/div/div/h1')
    assert error_message.text == 'The download limit has been exceeded.',\
        'Error message is not "The download limit has been exceeded."'

def check_login_page(driver):
    """Check transition destination is login page
    
    Args:
        driver(WebDriver): WebDriver object
    """
    # check transition destination is login page
    url = driver.current_url
    assert url.startswith(config.base_url + '/login'), 'Transition destination is not login page'

    # check next page is file detail page
    url_next = url.split('?next=')[1]
    assert url_next.find('file_details') != -1, 'Next page is not file detail page'

def check_secret_url_mail(driver, mail_address, item_name, expiration_date_num, download_limit):
    """Check secret url mail
    
    Args:
        driver(WebDriver): WebDriver object
        mail_address(str): mail address
        item_name(str): item name
        expiration_date_num(int): expiration date
        download_limit(int): download limit
    """
    # get target file name
    file_name = driver.find_element(
        By.XPATH,
        '//*[@id="detail-item"]/div[3]/div/div[2]/div/div/div[1]/table/tbody/tr/td[1]/span/a'
    ).text.split(' ')[0]

    # find target mail
    xs = []
    for root, _, files in os.walk('mail/root/new'):
        for file in files:
            path = os.path.join(root, file)
            xs.append((os.path.getmtime(path), path))
    target_mail = sorted(xs, reverse=True)[0][1]

    # check mail recipient
    with open(target_mail, 'r', encoding='utf-8') as f:
        lines = f.read().splitlines()
    recipient = [line for line in lines if line.startswith('To: ')]
    assert recipient[1].split(' ')[1] == mail_address

    # check mail body
    secret_url_info_jp = [line for line in lines if line.endswith('シークレットURLを作成しました。')]
    secret_url_info_en = [line for line in lines if line.startswith('Secret URL for')]
    limit_sentence_jp = [line for line in lines if line.startswith('このURLは')]
    limit_sentence_en = [line for line in lines if line.startswith('This URL is')]
    expiration_date = datetime.datetime.today() + datetime.timedelta(days=expiration_date_num)
    assert secret_url_info_jp[0].find(item_name) != -1\
        and secret_url_info_jp[0].find(file_name) != -1
    assert secret_url_info_en[0].find(item_name) != -1\
        and secret_url_info_en[0].find(file_name) != -1
    assert limit_sentence_jp[0].find(expiration_date.strftime('%Y-%m-%d')) != -1\
        and limit_sentence_jp[0].find(str(download_limit) + '回') != -1
    assert limit_sentence_en[0].find(expiration_date.strftime('%Y-%m-%d')) != -1\
        and limit_sentence_en[0].find(str(download_limit) + ' times') != -1

def check_secret_url_is_difference():
    """Check secret url is difference between the latest mail and the second latest mail"""
    # create path where mail is saved
    path = 'mail/root/new'

    # get all mail
    mail_list = os.listdir(path)

    # get the latest mail
    with open(path + '/' + mail_list[-1], 'r', encoding='utf-8') as f:
        text = f.read()
        latest_url = re.search('https://.*', text).group()

    # get the second latest mail
    with open(path + '/' + mail_list[-2], 'r', encoding='utf-8') as f:
        text = f.read()
        second_latest_url = re.search('https://.*', text).group()

    # compare the latest mail and the second latest mail
    assert latest_url != second_latest_url

def save_screenshot(driver, co_name):
    """Save screenshot
    
    Args:
        driver(WebDriver): WebDriver object
        co_name(str): test case name
    """
    time.sleep(1)
    driver.save_screenshot(
        config.base_save_folder + 'secret_url/' + d + "_" + co_name + ".png")
