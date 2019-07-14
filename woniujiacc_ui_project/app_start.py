from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '9'
desired_caps['deviceName'] = 'Redmi'
desired_caps['udid'] = '59ddcb00'
desired_caps['app'] = '/Users/mac/Desktop/monkeyrunner_test/hecr_debugsetting_debug.apk'
desired_caps['appPackage'] = 'com.jufuns.effectsoftware'
desired_caps['appActivity'] = 'com.jufuns.effectsoftware.act.SplashActivity'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
driver.implicitly_wait(15)

driver.find_element_by_id('com.jufuns.effectsoftware:id/act_login_edt_userName').send_keys('15616699600')
driver.find_element_by_id('com.jufuns.effectsoftware:id/act_login_edt_passWd').send_keys('123456')
driver.find_element_by_id('com.jufuns.effectsoftware:id/act_login_btn_login').click()
