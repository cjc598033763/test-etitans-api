# -*-coding:utf-8-*-
from lianxi2 import BaseOperator
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


class lianxi:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://arcb.com/tools/rate-quote.html#/new")
        self.zentao = BaseOperator(self.driver)
        self.driver.refresh()
        self.loc1 = ("xpath", "//div[4]/div/div[1]/abt-party/div/div[2]/div[1]/abt-city-coding-input//input")
        self.loc3 = ("xpath", "//ul[@role='listbox']/li")

    def test01(self):
        self.zentao.sendKeys(self.loc1, "98011")
        print(self.zentao.get_att(self.loc1,"value"))
        time.sleep(3)
        num = len(self.zentao.findElements(self.loc3))
        loc = []
        for i in range(1, num):
            loc2 = ("xpath", '//ul[@role="listbox"]/li[{num}]'.format(num=i))
            time.sleep(3)
            self.zentao.ActionChains_move(loc2)
            time.sleep(3)
            loc.append(self.zentao.get_ele_text(loc2))
            self.zentao.findElement(self.loc1).clear()
            self.zentao.sendKeys(self.loc1, "98011")
            print(loc)


if __name__ == '__main__':
    lianxi().test01()
