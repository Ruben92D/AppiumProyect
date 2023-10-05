from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

desired_caps = {}

desired_caps['platformName'] = 'Android'
desired_caps['automationName'] = 'UiAutomator2'
desired_caps['platformVersion'] = '13'
desired_caps['deviceName'] = 'Test'
desired_caps['app'] = ("C:/Users/Admin/Desktop/Appium_projects/Android_Demo_App.apk")
desired_caps['appPackage'] = 'com.code2lead.kwad'
desired_caps['appActivity'] = 'com.code2lead.kwad.MainActivity'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

ele_id = driver.find_element(AppiumBy.ID, "com.code2lead.kwad:id/EnterValue")
ele_id.click()