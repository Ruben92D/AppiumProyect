from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
import time
import pytest

from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait


@pytest.mark.flaky(reruns=5)
def test_runinAppium():
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

    crashBtn = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/crash")

    crashBtn.click()

    driver.quit()
