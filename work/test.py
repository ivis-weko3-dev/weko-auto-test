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
    A5(driver, 1)
    A6(driver)
    
    # 2~7は#1と同じ内容でロール（アカウント）が違うのみ
    # 2
    # 3
    # 4
    # 5
    # 6
    # 7

    # 8
    A5(driver, 2)
    A6(driver)
    
    # 9~14は#8と同じ内容でロール（アカウント）が違うのみ
    # 9
    # 10
    # 11
    # 12
    # 13
    # 14
    
    # 15
    A5(driver, 3)
    A6(driver)
    
    # 16
    A5(driver, 3)
    A7(driver)
    
    # 17
    A8(driver, "root")
    
    # 18
    for i in range(3):
        A8(driver, "root")
        
    # 20
    A5(driver, 3)
    A7(driver)
    
    # 21~26は#15~#20と同じ内容でロール（アカウント）が違うのみ
    # 21
    # 22
    # 23
    # 24
    # 26
    
    # 27~31は#15と同じ内容でロール（アカウント）が違うのみ
    # 27
    # 28
    # 29
    # 30
    # 31
    
    # 32
    A5(driver, 4)
    A6(driver)
    
    # 33~38は#32と同じ内容でロール（アカウント）が違うのみ
    # 33
    # 34
    # 35
    # 36
    # 37
    # 38
    
    # 39
    A5(driver, 4)
    A6(driver)
    
    # 40
    A7(driver)
    # mail/root/newフォルダにメールが届く
    
    # 41
    A8(driver, "root")
    # downloadsフォルダにコンテンツがダウンロードされる
    
    # 42
    A8(driver, "root")
    A8(driver, "root")
    A8(driver, "root")
    
    # 44
    A5(driver, 4)
    A6(driver)
    A7(driver)
    
    # 45~50は#39~#44と同じ内容でロール（アカウント）が違うのみ
    # 45
    # 46
    # 47
    # 48
    # 50
    
    # 51~55は#39と同じ内容でロール（アカウント）が違うのみ
    # 51
    # 52
    # 53
    # 54
    # 55
    
    # 56
    A5(driver, 1)
    A6(driver)
    
    # 57~62は#56と同じ内容でロール（アカウント）が違うのみ
    # 57
    # 58
    # 59
    # 60
    # 61
    # 62
    
    # 63
    A5(driver, 2)
    A6(driver)
    
    # 64~69は#63と同じ内容でロール（アカウント）が違うのみ
    # 64
    # 65
    # 66
    # 67
    # 68
    # 69
    
    # 70
    A5(driver, 3)
    A6(driver)
    
    # 71~76は#70と同じ内容でロール（アカウント）が違うのみ
    # 71
    # 72
    # 73
    # 74
    # 75
    # 76
    
    # 77
    A5(driver, 4)
    A6(driver)
    
    # 78~83は#77と同じ内容でロール（アカウント）が違うのみ
    # 78
    # 79
    # 80
    # 81
    # 82
    # 83
    
    # 84
    A5(driver, 5)
    A6(driver)
    
    # 85~90は#84と同じ内容でロール（アカウント）が違うのみ
    # 85
    # 86
    # 87
    # 88
    # 89
    # 90
    
    # 91
    A2(driver, True)
    
    A5(driver, 3)
    A6(driver)
    A7(driver)
    A2(driver, False)
    time.sleep(1)
    A8(driver, "root")
    
    # 92は#91と同じ内容でロール（アカウント）が違うのみ
    # 92
    
    # 93
    A2(driver, True)
    
    A5(driver, 5)
    A6(driver)
    A7(driver, True)
    A2(driver, False)
    A8(driver, "root")
    
    # 94は#93と同じ内容でロール（アカウント）が違うのみ
    # 94
    
    # 95
    A4(driver, 3)
    
    A5(driver, 3)
    A6(driver)
    A7(driver)
    
    A4(driver, 5)
    
    for i in range(6):
        A8(driver, "root")
        
    # 96は#95と同じ内容でロール（アカウント）が違うのみ
    # 96
    
    # 97
    A4(driver, 3)
    
    A5(driver, 5)
    A6(driver)
    A7(driver, True)
    
    A4(driver, 5)
    
    for i in range(6):
        A8(driver, "root")

    # 98は#97と同じ内容でロール（アカウント）が違うのみ
    # 98
    
    # 99~102
    
    
def test_application_function(driver):
    # 1
    A5(driver, 6)
    
    # 2
    A10(driver)
    
    # 3
    
    # 4は#1と同じ内容でロール（アカウント）が違うのみ
    # 4
    
    # 5は#2と同じ内容でロール（アカウント）が違うのみ
    # 5
    
    # 6は#1と同じ内容でロール（アカウント）が違うのみ
    # 6
    
    # 7は#2と同じ内容でロール（アカウント）が違うのみ
    # 7
    
    # 8
    
    # 9は#1と同じ内容でロール（アカウント）が違うのみ
    # 9
    
    # 10は#2と同じ内容でロール（アカウント）が違うのみ
    # 10
    
    # 11は#1と同じ内容でロール（アカウント）が違うのみ
    # 11
    
    # 12は#2と同じ内容でロール（アカウント）が違うのみ
    # 12
    
    # 13
    A11(driver)
    
    # 14
    A13(driver)
    
    # 15
    A12(driver)
    A13(driver)
    
    # 16
    
    # 17は#1と同じ内容でロール（アカウント）が違うのみ
    # 17
    
    # 18
    A5(driver, 7)
    
    # 19
    A10(driver)
    
    # 20
    
    # 21は#18と同じ内容でロール（アカウント）が違うのみ
    # 21
    
    # 22は#19と同じ内容でロール（アカウント）が違うのみ
    # 22
    
    # 23は#18と同じ内容でロール（アカウント）が違うのみ
    # 23
    
    # 24は#19と同じ内容でロール（アカウント）が違うのみ
    # 24
    
    # 25
    
    # 26は#18と同じ内容でロール（アカウント）が違うのみ
    # 26
    
    # 27は#19と同じ内容でロール（アカウント）が違うのみ
    # 27
    
    # 28は#18と同じ内容でロール（アカウント）が違うのみ
    # 28
    
    # 29は#19と同じ内容でロール（アカウント）が違うのみ
    # 29
    
    # 30は#18と同じ内容でロール（アカウント）が違うのみ
    # 30
    
    # 31は#19と同じ内容でロール（アカウント）が違うのみ
    # 31
    
    # 32
    A11(driver)
    
    # 33
    A13(driver)
    
    # 34
    A12(driver)
    A13(driver)
    
    # 35
    
    # 36
    for i in range(10):
        A11(driver)
        A12(driver)
        A13(driver)
        
    # 37
    A5(driver, 8)
    
    # 38
    A10(driver)
    
    # 39
    
    # 40は#37と同じ内容でロール（アカウント）が違うのみ
    # 40
    
    # 41は#38と同じ内容でロール（アカウント）が違うのみ
    # 41
    
    # 42は#37と同じ内容でロール（アカウント）が違うのみ
    # 42
    
    # 43は#38と同じ内容でロール（アカウント）が違うのみ
    # 43
    
    # 44
    
    # 45は#37と同じ内容でロール（アカウント）が違うのみ
    # 45
    
    # 46は#38と同じ内容でロール（アカウント）が違うのみ
    # 46
    
    # 47は#37と同じ内容でロール（アカウント）が違うのみ
    # 47
    
    # 48#38と同じ内容でロール（アカウント）が違うのみ
    # 48
    
    # 49
    A11(driver)
    
    # 50
    A13(driver)
    
    # 51
    A12(driver)
    A13(driver)
    
    # 52
    A15(driver)
    
    # 53
    

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