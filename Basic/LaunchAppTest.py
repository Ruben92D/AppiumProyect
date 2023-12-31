from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
import time

appium_service = AppiumService()

appium_service.start()

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'platformVersion': '13',
    'deviceName': 'Test2',
    'automationName': 'UiAutomator2',
    'app': ("C:/Users/Admin/Desktop/Appium_projects/Android_Demo_App.apk"),
    'appPackage': 'com.code2lead.kwad',
    'appActivity': 'com.code2lead.kwad.MainActivity',
    'autoAcceptAlerts': 'true',  # to accept all alerts
    'autoGrantPermissions': 'true'
}

url = 'http://127.0.0.1:4723'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

ele_id = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Btn2"]')
ele_id.click()
time.sleep(5)
driver.quit()

appium_service.stop()