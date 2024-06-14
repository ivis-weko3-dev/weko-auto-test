from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.alert import Alert
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
import time
import datetime
import os
import re
import config

d = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%s")

def is_integer(n):
    try:
        float(n)
    except ValueError:
        return False
    else:
        return float(n).is_integer()

def logout(driver):
    driver.get(config.base_url + "/logout/")
    time.sleep(1)
    
def until_complete_download(time_limit):
    for x in range(time_limit):
        file_list = os.listdir(config.base_download_dir)
        for filename in file_list:
            if re.search(r".*\.com\.google\.Chrome.*", filename) != None or re.search(r".*\.crdownload", filename) != None:
                # print(re.search(r"\.com\.google\.Chrome.*", filename), re.search(r"\.crdownload", filename))
                time.sleep(1)
                if x == time_limit - 1:
                    raise Exception(f"Download did not complete within {time_limit} seconds")
                break
            
def select_WF(driver):
    driver.find_element(By.XPATH, '//*[@id="background-color-main-content"]/ul/li[2]/a').click()
    
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="myTabContent"]/div[4]/div/div[1]/table/tbody/tr[1]/td[5]/a').click()
    
            

# SecretURL
def A1(driver, account_mail, account_password):
    """login.

    :param driver: webdriver
    :param account_mail
    :param account_password
    """
    # access to WEKO's TOP page
    driver.get(config.base_url)
    driver.implicitly_wait(10)
    
    # show Login page with press login button
    driver.find_element(By.XPATH, '//*[@id="fixed_header"]/form/a[1]').click()
    driver.implicitly_wait(10)
    
    # enter mail-address and password and click login button
    driver.find_element(By.XPATH, '//*[@id="email"]').send_keys(account_mail)
    driver.find_element(By.XPATH, '//*[@id="password"]').send_keys(account_password)
    driver.find_element(By.XPATH, '/html/body/div/div[2]/div/div/div/div[1]/form/button').click()
    
    time.sleep(1)
    
def A2(driver, enable):
    """Set SecretURL ON/OFF.

    :param driver: webdriver
    :param enable: boolean
    """
    # access to Administration/restricted access page
    driver.get(config.base_url + "/admin/restricted_access/")
    driver.implicitly_wait(10)
    
    # click 'SecretURL enable/disable button'
    check_box = driver.find_element(By.XPATH, '//*[@id="secret_enable"]')
    if (check_box.get_attribute("checked") == "true") != enable:
        check_box.click()
        driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
    
    time.sleep(1)
    
def A3(driver, expiration_date, expiration_date_unlimited = False):
    """change expiration_date.

    :param driver: webdriver
    :param expiration_date
    :param expiration_date_unlimited
    """
    # access to Administration/restricted access page
    driver.get(config.base_url + "/admin/restricted_access/")
    driver.implicitly_wait(10)
    
    # check if SecretURL is enabled
    check_box = driver.find_element(By.XPATH, '//*[@id="secret_enable"]')
    if check_box.get_attribute("checked") == "true":
        if expiration_date_unlimited:
            expiration_date_unlimited_check = driver.find_element(By.XPATH, '//*[@id="secret_expiration_date_unlimited_chk"]')
            # set expiration_date_unlimited_checkbox if it is disabled
            if expiration_date_unlimited_check.get_attribute("checked") != "true":
                expiration_date_unlimited_check.click()
                driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
        else:
            if is_integer(expiration_date):
                # change expiration_date
                driver.find_element(By.XPATH, '//*[@id="secret_expiration_date"]').clear()
                driver.find_element(By.XPATH, '//*[@id="secret_expiration_date"]').send_keys(expiration_date)
                driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
            else:
                print("Expiration Date must be an integer")
    else:
        print("Secret URL is not enable")
        
    time.sleep(1)
    
def A4(driver, download_limit, download_limit_unlimited = False):
    """change download_limit count.

    :param driver: webdriver
    :param download_limit
    :param download_limit_unlimited
    """
    # access to Administration/restricted access page
    driver.get(config.base_url + "/admin/restricted_access/")
    driver.implicitly_wait(10)
    
    # check if SecretURL is enabled
    check_box = driver.find_element(By.XPATH, '//*[@id="secret_enable"]')
    if check_box.get_attribute("checked") == "true":
        if download_limit_unlimited:
            download_limit_unlimited_check = driver.find_element(By.XPATH, '//*[@id="secret_download_limit_unlimited_chk"]')
            if download_limit_unlimited_check.get_attribute("checked") != "true":
                # set download_limit_unlimited_checkbox if it is disabled
                download_limit_unlimited_check.click()
                driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
        else:
            if is_integer(download_limit):
                driver.find_element(By.XPATH, '//*[@id="secret_download_limit"]').clear()
                driver.find_element(By.XPATH, '//*[@id="secret_download_limit"]').send_keys(download_limit)
                driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()
            else:
                print("Download Limit must be an integer")
    else:
        print("Secret URL is not enable")
        
    time.sleep(1)

def A5(driver, record_id):
    """access to Item details page.

    :param driver: webdriver
    :param record_id
    """
    driver.get(config.base_url + "/records/" + str(record_id))
    time.sleep(1)
    
def A6(driver):
    """access to file information page.

    :param driver: webdriver
    """
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]/a[2]/button').click()
    
    time.sleep(1)
    
    # driver.save_screenshot(
    #     config.base_save_folder + d + "_test6.png"
    # )
    
def A7(driver, save_ss = False):
    """click SecretURL button.

    :param driver: webdriver
    """
    driver.find_element(By.XPATH, '//*[@id="secret_url"]').click()
    
    wait = WebDriverWait(driver, timeout=10)
    wait.until(expected_conditions.alert_is_present())
    
    # if save_ss:
    #     driver.save_screenshot(
    #         config.base_save_folder + d + "_test_alert.png"
    #     )
    
    driver.switch_to.alert.accept()
    
    # driver.save_screenshot(
    #     config.base_save_folder + d + "_test7.png"
    # )
    
    time.sleep(1)
    
def A8(driver, user):
    """click link in mail.

    :param driver: webdriver
    :param user: user maildir folder name
    """
    mail_list = os.listdir("mail/" + user + "/new")
    
    with open("mail/" + user + "/new/" + mail_list[-1], "r") as f:
        text = f.read()
        url = re.search("https://.*", text).group()
        driver.get(url)
        
    try:
        until_complete_download(10)
    except Exception as e:
        print(e)
    time.sleep(1)
    
# ダウンロードボタンまたは利用申請ボタン押下
def A10(driver):
    driver.find_element(By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]/a[1]/button').click()
    
# プリントボタン押下
def A11(driver):
    driver.find_element(By.XPATH, '//*[@id="print-btn"]').click()
    
# 利用規約チェック
def A12(driver):
    try:
        driver.find_element(By.CLASS_NAME, 'pointer').click()
    except:
        # driver.find_element(By.XPATH, '//*[@id="allModal"]/div/div/div[3]/button'):
        return
    
# 利用規約ダイアログの「次へ」ボタン押下
def A13(driver):
    driver.find_element(By.CLASS_NAME, 'term_next').click()
    
# 利用申請メール入力・送信
def A14(driver, guest_mail):
    driver.find_element(By.XPATH, '//*[@id="user_mail"]').send_keys(guest_mail)
    driver.find_element(By.XPATH, '//*[@id="user_mail_confirm"]').send_keys(guest_mail)
    driver.find_element(By.XPATH, '//*[@id="confirm_email_btn"]').click()
    time.sleep(1)
    driver.find_element(By.XPATH, '//*[@id="modalSendEmailSuccess"]/div/div/div[3]/div/button').click()
        
# WF入力
def A15(driver):
    # 利用申請ワークフロー、「次へ」ボタン押下
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="weko_records_ctrl"]/div[8]/div/div[1]/div/button[2]/span').click()
    
    # インデックスツリー登録後「次へ」ボタン押下
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="step_page"]/div[2]/div/app-root-tree/app-tree-list2/div[2]/div/div[1]/div/div/div[2]/tree/tree-internal/ul/li/tree-internal/ul/li/div/div[2]/input').click()
    driver.find_element(By.XPATH, '//*[@id="step_page"]/div[2]/div/app-root-tree/app-tree-list2/div[2]/div/div[2]/div/div/div[3]/button[2]').click()
    
    # 「次へ」ボタン押下
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="btn-finish"]').click()
    
    # 「次へ」ボタン押下
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="step_page_permission"]/div/div/div/h1')
    
# WF承認
def A16(driver):
    driver.find_element(By.XPATH, '//*[@id="btn-approval"]').click()
     
# WF却下
def A17(driver):
    driver.find_element(By.XPATH, '//*[@id="btn-reject"]').click()
    
# 利用申請承認後のゲストでのDL（メールアドレス入力）
def A18(driver, guest_mail):
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="mail_form"]').send_keys(guest_mail)
    driver.find_element(By.XPATH, '//*[@id="mailaddress_confirm_download"]').click()
    
# WF保存ボタン押下
def A19(driver):
    driver.find_element(By.XPATH, '//*[@id="weko_records_ctrl"]/div[8]/div/div[1]/div/button[2]').click()
    
# WF強制終了ボタン押下
def A20(driver):
    driver.find_element(By.XPATH, '//*[@id="btn_quit"]').click()

def B1(driver):
    # 管理者画面表示
    driver.find_element(By.XPATH, '//*[@id="fixed_header"]/div[2]/div/button').click()
    driver.find_element(By.XPATH, '//*[@id="fixed_header"]/div[2]/div/ul/li[6]').click()
    
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '/html/body/div/aside/section/ul/li[15]').click()
    driver.find_element(By.XPATH, '/html/body/div/aside/section/ul/li[15]/ul/li[17]').click()
    
    driver.implicitly_wait(10)
    driver.find_element(By.XPATH, '//*[@id="new_term"]').click()
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[1]/input').send_keys("aaa")
    driver.find_element(By.XPATH, '//*[@id="root"]/div/div[1]/div[2]/div/div/div[2]/textarea').send_keys("sample text")


def transition_to_mail_template(driver):
    """Transition to Mail Template page
    
    Args:
        driver(WebDriver): WebDriver object
    """
    driver.get(config.base_url + "/admin/mailtemplates/")
    time.sleep(1)

def set_secret_url(driver, param):
    """Set SecretURL Status.

    Args:
        driver(WebDriver): WebDriver object
        param(bool): On(True) or OFF(False)
    """
    # access to Administration/restricted access page
    driver.get(config.base_url + "/admin/restricted_access/")
    driver.implicitly_wait(10)

    # click 'SecretURL enable button' if its checked is not equal to param
    check_box = driver.find_element(By.XPATH, '//*[@id="secret_enable"]')
    if bool(check_box.get_attribute("checked")) != param:
        check_box.click()
        driver.find_element(By.XPATH, '//*[@id="save-btn"]').click()

    time.sleep(1)

def transition_to_restricted_access(driver):
    """Transition to Restricted Access page
    
    Args:
        driver(WebDriver): WebDriver object
    """
    driver.get(config.base_url + "/admin/restricted_access/")
    time.sleep(1)

def search_and_display_target_item(driver, param):
    # access to WEKO's TOP page
    driver.get(config.base_url)

    # search target item
    search_box = driver.find_element(By.XPATH, '//*[@id="q"]')
    search_box.send_keys(param)
    driver.find_element(By.XPATH, '//*[@id="top-search-btn"]').click()
    time.sleep(1)

    # display target item
    search_result = driver.find_element(
        By.XPATH, '//*[@id="index_item_list"]/div[2]/div/div/invenio-search-results')
    search_result_list = search_result.find_elements(By.CLASS_NAME, 'panel')
    for result in search_result_list:
        header = result.find_element(By.XPATH, './/div/div/a')
        if header.text == param:
            header.click()
            break

    time.sleep(1)

def click_file_information_button(driver):
    button_list = driver.find_element(
        By.XPATH, '//*[@id="detail-item"]/table/tbody/tr/td[3]').find_elements(By.TAG_NAME, 'a')
    for button in button_list:
        if button.text == 'Information':
            button.click()
            break
    time.sleep(1)
    
def main():
    try:
        setup_driver = config.SetupDriver()
        setup_driver.setup_driver()
        
        A1(setup_driver.driver, config.test_account_mail, config.test_account_password)

        time.sleep(1)
        setup_driver.teardown_method()
    except Exception as ex:
        print(ex)
        setup_driver.teardown_method()

if __name__ == "__main__":
    main()