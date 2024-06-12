from selenium import webdriver
import config
import time
from methods_required_during_testing import *

# options = webdriver.ChromeOptions()
# driver = webdriver.Remote(
#     command_executor="http://selenium:4444/wd/hub", options=options
# )

# driver.implicitly_wait(10)

# # url = 'https://google.com/' # テストでアクセスするURLを指定
# url = config.base_url
# driver.get(url)

# time.sleep(3)
# driver.save_screenshot(
#     config.base_save_folder + "test.png"
# )  # アクセスした先でスクリーンショットを取得
# driver.quit()

def test_secretURL(driver):
    A1(driver, config.test_account_mail, config.test_account_password)
    
    # 1
    # A5(driver, 1)
    # A6(driver)
    
    # driver.save_screenshot(
    #     config.base_save_folder + d + "_test1.png"
    # )

    # # 8
    # A5(driver, 2)
    # A6(driver)
    
    # driver.save_screenshot(
    #     config.base_save_folder + d + "_test8.png"
    # )
    
    # # 15
    # A5(driver, 3)
    # A6(driver)
    
    # driver.save_screenshot(
    #     config.base_save_folder + d + "_test15.png"
    # )
    
    # # 39
    # A5(driver, 4)
    # A6(driver)
    
    # driver.save_screenshot(
    #     config.base_save_folder + d + "_test39.png"
    # )
    
    # # 40
    # A7(driver)
    # # mail/root/newフォルダにメールが届く
    
    # # 41
    # A8(driver, "root")
    # # downloadsフォルダにコンテンツがダウンロードされる
    
    # # 42
    # A8(driver, "root")
    # A8(driver, "root")
    # A8(driver, "root")
    # driver.save_screenshot(
    #     config.base_save_folder + d + "_test42.png"
    # )
    
    # # 43
    
    # # 44
    # A5(driver, 4)
    # A6(driver)
    # A7(driver)
    
    # 93
    # A5(driver, 4)
    # A6(driver)
    # A7(driver, True)
    # A2(driver)
    # A8(driver, "root")
    # driver.save_screenshot(
    #     config.base_save_folder + d + "_test93.png"
    # )
    
    # 97
    # A5(driver, 4)
    # A6(driver)
    # A7(driver, True)
    
    # A4(driver, 5)
    
    # A8(driver, "root")
    # A8(driver, "root")
    # A8(driver, "root")
    # A8(driver, "root")
    # A8(driver, "root")
    # A8(driver, "root")
    # driver.save_screenshot(
    #     config.base_save_folder + d + "_test97.png"
    # )
    
    # test
    logout(driver)
    A5(driver, 1)
    A10(driver, config.guest_mail)
    
    
    

def main():
    try:
        setup_driver = config.SetupDriver()
        setup_driver.setup_driver()
        
        test_secretURL(setup_driver.driver)

        time.sleep(1)
        setup_driver.driver.save_screenshot(
            config.base_save_folder + d + "_test97.png"
        )
        
        setup_driver.teardown_method()
        
    except Exception as ex:
        print(ex)
        setup_driver.driver.save_screenshot(
            config.base_save_folder + d + "_error.png"
        )
        setup_driver.teardown_method()

if __name__ == "__main__":
    main()