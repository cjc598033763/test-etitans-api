# -*-coding:utf-8-*-
import time
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

from selenium.webdriver.support import expected_conditions as EC


class BaseOperator():

    def __init__(self, driver=None, url="https://arcb.com/tools/rate-quote.html#/new"):
        if not driver:
            driver=webdriver.Chrome()
        self.driver=driver
        self.driver.set_window_size(1552,840)
        self.driver.implicitly_wait(10)
        self.driver.get(url)
        self.timeout=5
        self.t=0.01

    def implicitly_wait(self):
        self.driver.implicitly_wait(30)

    def quit(self):
        self.driver.quit()

    def findElementNew(self, locator):

        ele=WebDriverWait(self.driver, self.timeout, self.t).until(EC.presence_of_element_located(locator))
        return ele

    def get_att(self, locator, value):  # 获取输入的文本值
        ele=self.findElement(locator)
        return ele.get_attribute(value)

    def refresh(self):
        self.driver.refresh()
        time.sleep(0.5)

    def get_ele_text(self, locator):
        ele=self.findElement(locator).text
        return ele

    def findElement(self, locator):
        ele=WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_element(*locator))
        return ele

    def findElements(self, locator):
        try:
            eles=WebDriverWait(self.driver, self.timeout, self.t).until(lambda x: x.find_elements(*locator))
            return eles
        except:
            return []

    def sendKeys(self, locator, text):
        ele=self.findElement(locator)
        ele.send_keys(text)

    def click(self, locator):
        ele=self.findElement(locator)
        ele.click()

    def clear(self, locator):
        ele=self.findElement(locator)
        ele.clear()

    def isSelected(self, locator):

        ele=self.findElement(locator)
        r=ele.is_selected()
        return r

    def isElementExist(self, locator):
        try:
            self.findElement(locator)
            return True
        except:
            return False

    def isElementExist2(self, locator):
        eles=self.findElements(locator)
        n=len(eles)
        if n == 0:
            return False
        elif n == 1:
            return True
        else:
            return n

    def is_title(self, _title):

        try:
            result=WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_is(_title))
            return result
        except:
            return False

    def is_title_contains(self, _title):

        try:
            result=WebDriverWait(self.driver, self.timeout, self.t).until(EC.title_contains(_title))
            return result
        except:
            return False

    def is_text_in_element(self, locator, _text):

        try:
            result=WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element(locator, _text))
            return result
        except:
            return False

    def is_value_in_element(self, locator, _value):

        try:
            result=WebDriverWait(self.driver, self.timeout, self.t).until(
                EC.text_to_be_present_in_element_value(locator, _value))
            return result
        except:
            return False

    def is_alert(self):
        try:
            result=WebDriverWait(self.driver, self.timeout, self.t).until(EC.alert_is_present())
            return result
        except:
            return False

    def method_click(self, loctor):
        self.driver.execute_script("arguments[0].click();", self.findElement(loctor))

    def ActionChains_move(self, loc):
        ActionChains(self.driver).move_to_element(self.findElement(loc)).perform()

    def source(self,loc):
        return self.findElement(loc).get_attribute('innerHTML')