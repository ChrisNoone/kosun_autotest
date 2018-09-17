# -*- coding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

locator = (By.CLASS_NAME, "menuRow")

driver = webdriver.Chrome()
driver.get("https://fusion.spmobileapi.net/dglobby#/")
driver.maximize_window()
time.sleep(5)
try:
    WebDriverWait(driver, 10, 1).until(EC.presence_of_all_elements_located(locator))

    '''
    driver.find_element_by_xpath("//*[@class = 'hallMenu']/div[contains(text(), 'PC蛋蛋')]").click()
    time.sleep(1)
    playName = "五分28"
    driver.find_element_by_xpath("//*[text() = '%s']/../../..//*[text() = '立即购彩']" % playName).click()
    time.sleep(2)
    driver.find_element_by_xpath("//*[@class = 'tema']//*[text() = '0']/../../div[@class = 'money']/input").send_keys("20")
    time.sleep(1)
    driver.find_element_by_xpath("//*[text() = '添加注单']").click()
    time.sleep(1)
    driver.find_element_by_xpath("//*[text() = '确认投注']").click()
    time.sleep(10)
    '''
finally:
    driver.close()
