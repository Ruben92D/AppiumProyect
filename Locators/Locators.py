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

# ele_index = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, "UiSelector().index(4)")
# ele_index.click()
# time.sleep(2)

# ele_classname = driver.find_element(AppiumBy.CLASS_NAME, "android.widget.EditText")
# ele_classname.send_keys("test")

# ele_name = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().text("ScrollView")')
# # ele_name = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'text("ScrollView")')
# ele_name.click()

# ele_description = driver.find_element(AppiumBy.ANDROID_UIAUTOMATOR, 'UiSelector().description("Btn4")')
# ele_description.click()

# ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[@content-desc="Btn1"]') atributo y valor
# ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[1]') por indice
# ele_xpath = driver.find_element(AppiumBy.XPATH, '//android.widget.Button[1]') # por clase
# ele_xpath.click()
# ele_input = driver.find_element(AppiumBy.XPATH, '//android.widget.EditText')
# ele_input.send_keys("test")

# elements = driver.find_elements(AppiumBy.CLASS_NAME, ("android.widget.Button"))
# for x in elements:
#     print(x.text)
#     button = x.text
#     if button == "ENTER SOME VALUE":
#         x.click()
#         break

# wait = WebDriverWait(driver, 25, poll_frequency=1, ignored_exceptions=[ElementNotVisibleException, ElementNotSelectableException, NoSuchElementException])
# ele = wait.until(lambda x: x.find_element(AppiumBy.CLASS_NAME, "android.widget.Button"))
# ele.click()
# ele_input = wait.until(lambda x: x.find_element(AppiumBy.XPATH, '//android.widget.EditText'))

ele = WebDriverWait(driver, 25).until(EC.presence_of_element_located((By.ID, 'com.code2lead.kwad:id/EnterValue')))
ele.click()

time.sleep(5)
driver.quit()

#appium_service.stop()