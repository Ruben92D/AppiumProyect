from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy
from appium.webdriver.appium_service import AppiumService
import time

from appium.webdriver.common.touch_action import TouchAction
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
wait = WebDriverWait(driver, 25, 1, [ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
actions = TouchAction(driver)

print("device size: ", driver.get_window_size())

deviceSize = driver.get_window_size()
screenWidth = deviceSize['width']
screenHeight = deviceSize['height']

### Right to left
startx = screenWidth*8/9
endx = screenWidth/9
starty = screenHeight/2
endy = screenHeight/2

### Left to right
startx2 = screenWidth/9
endx2 = screenWidth*8/9
starty2 = screenHeight/2
endy2 = screenHeight/2


tabActBtn = wait.until(lambda x: x.find_element(AppiumBy.ID, "com.code2lead.kwad:id/TabView"))
tabActBtn.click()
time.sleep(2)

actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()

time.sleep(2)

actions.long_press(None, startx2, starty2).move_to(None, endx2, endy2).release().perform()

gobackbtn = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, "android.widget.ImageButton"))

gobackbtn.click()

time.sleep(2)

### Bottom to top
startx = screenWidth/2
endx = screenWidth/2
starty = screenHeight*8/9
endy = screenHeight/9

### Top to bottom
startx2 = screenWidth/2
endx2 = screenWidth/2
starty2 = screenHeight*2/9
endy2 = screenHeight*8/9

time.sleep(2)

actions.long_press(None, startx, starty).move_to(None, endx, endy).release().perform()

time.sleep(2)

actions.long_press(None, startx2, starty2).move_to(None, endx2, endy2).release().perform()



