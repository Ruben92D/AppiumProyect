from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
from selenium.webdriver.common.by import By
import time

from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

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

print("Current package", driver.current_package)
print("Current activity", driver.current_activity)
print("Current context", driver.current_context)
print("Current orientation", driver.orientation)