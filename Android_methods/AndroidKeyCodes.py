import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

appium_service = AppiumService()

#appium_service.start()

cap: Dict[str, Any] = {
    'platformName': 'Android',
    'platformVersion': '13',
    'deviceName': 'Pixel XL',
    'automationName': 'UiAutomator2',
    'app': ("C:/Users/Admin/Desktop/Appium_projects/Android_Demo_App.apk"),
    'appPackage': 'com.code2lead.kwad',
    'appActivity': 'com.code2lead.kwad.MainActivity',
    'autoAcceptAlerts': 'true',  # to accept all alerts
    'autoGrantPermissions': 'true'
}

url = 'http://127.0.0.1:4723/wd/hub'
driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))
ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Btn1"]')
ele_xpath.click()
wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
ele = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/Et1"))
# ele_input = driver.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/Et1')
ele.send_keys("test")
ele.click()

driver.press_keycode(67)
driver.press_keycode(4)
driver.press_keycode(4)
time.sleep(2)