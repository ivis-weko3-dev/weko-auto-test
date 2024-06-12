import sys

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
    login(driver, 'C1')

    # Flow 1
    # Secret URL enable, Expiration Date is 3, Download Limit is 3
    set_secret_url(driver, True)
    A3(driver, 3)
    A4(driver, 3)

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C3')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C4')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C5')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C2')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C6')

    # search target item
    search_and_display_target_item(driver, 'B1_オープンアクセス')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C1')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C3')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C4')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check error page
    check_error_page(driver)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C5')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C2')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check error page
    check_error_page(driver)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C6')

    # search target item
    search_and_display_target_item(driver, 'B2_制限公開')

    # display content's info
    click_file_information_button(driver)

    # check error page
    check_error_page(driver)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C1')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is not hidden
    check_secret_url_button_is_hidden(driver, False)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C3')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is not hidden
    check_secret_url_button_is_hidden(driver, False)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C4')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check error page
    check_error_page(driver)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C5')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C2')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check error page
    check_error_page(driver)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C6')

    # search target item
    search_and_display_target_item(driver, 'B3_公開前')

    # display content's info
    click_file_information_button(driver)

    # check error page
    check_error_page(driver)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C1')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C3')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C4')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C5')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

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
    login(driver, 'C2')

    # search target item
    search_and_display_target_item(driver, 'B4_公開後')

    # display content's info
    click_file_information_button(driver)

    # check secret url button is hidden
    check_secret_url_button_is_hidden(driver, True)

    save_screenshot(driver, sys._getframe().f_code.co_name)

def test_no_37(driver):
    """No.37 Secret URL button is hidden"""

def login(driver, target_key):
    # set login_user from config
    login_user = config.secret_url_users[target_key]
    # log in as target user
    A1(driver, login_user['mail'], login_user['password'])


def check_secret_url_button_is_hidden(driver, is_hidden):
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

def check_error_page(driver):
    # check error page does't have weko's panel component
    components = driver.find_elements(By.XPATH, '//*[@id="panel-main-content"]')
    assert len(components) == 0, 'This page is not error page'

    # check error page has the class what name is error-page
    error_page = driver.find_elements(By.CLASS_NAME, 'error-page')
    assert len(error_page) > 0, 'This page is not error page'

    # check error message
    error_message = error_page[0].find_element(By.XPATH, './/div/div/h1')
    assert error_message.text == 'Permission required', 'Error message is not "Permission required"'

def check_login_page(driver):
    # check transition destination is login page
    url = driver.current_url
    assert url.startswith(config.base_url + '/login'), 'Transition destination is not login page'

    # check next page is file detail page
    url_next = url.split('?next=')[1]
    assert url_next.find('file_details') != -1, 'Next page is not file detail page'

def save_screenshot(driver, co_name):
    time.sleep(1)
    driver.save_screenshot(
        config.base_save_folder + 'secret_url/' + d + "_" + co_name + ".png")
