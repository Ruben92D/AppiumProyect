import time

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

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
wait = WebDriverWait(driver, 25, 1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException,
                                                        NoSuchElementException])
ele = driver.find_element(AppiumBy.CLASS_NAME, 'android.widget.Button')

print("Text on the button: ", ele.text)
print("Text on the button: ", ele.get_attribute("text"))
print("Text on the button: ", ele.get_attribute("content-desc"))

ele.click()

eleInput = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, 'android.widget.EditText'))

eleInput.send_keys("test")
eleInput.clear()
