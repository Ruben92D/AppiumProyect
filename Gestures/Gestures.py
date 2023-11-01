from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
import time

from appium.webdriver.common.touch_action import TouchAction
from selenium.common import ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException
from selenium.webdriver.support.wait import WebDriverWait

# appium_service = AppiumService()
#
# appium_service.start()

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
wait = WebDriverWait(driver, 25, 1, [ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
scrollBtn = driver.find_element(AppiumBy.ID, 'com.code2lead.kwad:id/ScrollView')
scrollBtn.click()

#Scroll into view
btnSixteen = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR,'new UiScrollable(new UiSelector()).scrollIntoView(text("BUTTON16"))'))

btnSixteen.click()

yespopupbtn = wait.until(lambda x: x.find_element(AppiumBy.ID, 'android:id/button1'))

yespopupbtn.click()
#long click

actions = TouchAction(driver)
longClikBtn = wait.until(lambda x: x.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'new UiScrollable(UiSelector().text("LONG CLICK"))'))
actions.long_press(longClikBtn,5)
actions.perform()


time.sleep(2)


# appium_service.stop()