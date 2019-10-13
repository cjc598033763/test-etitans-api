# -*-coding:utf-8-*-
import self as self

from lianxi2 import BaseOperator
from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains


class lianxi:
    def __init__(self):
        option=webdriver.ChromeOptions()
        option.add_argument('disable-infobars')
        option.add_argument('--headless')
        option.add_argument('--incognito')
        option.add_argument('--no-sandbox')
        self.driver=webdriver.Chrome(chrome_options=option)
        self.driver.get("https://arcb.com/tools/rate-quote.html#/new")
        self.zentao=BaseOperator(self.driver)
        self.driver.refresh()
        self.loc1=("xpath", "//div[4]/div/div[1]/abt-party/div/div[2]/div[1]/abt-city-coding-input//input")
        self.loc3=("xpath", "//ul[@role='listbox']/li")

    def read_txt(self):
        f=open("regions.txt", "r")
        line=f.readlines()
        return str(line).replace("\\n", "").replace("'", "")

    def test01(self):
        self.a=eval(self.read_txt())
        # self.a=["00501","25045"]
        self.loc=[]
        time.sleep(15)
        for n in self.a:
            time.sleep(0.5)
            self.zentao.sendKeys(self.loc1, str(n))
            num=len(self.zentao.findElements(self.loc3))
            if num > 0:
                for i in range(1, num + 1):
                    loc2=("xpath", '//ul[@role="listbox"]/li[{num}]'.format(num=i))

                    self.zentao.ActionChains_move(loc2)
                    self.loc.append(self.zentao.get_ele_text(loc2))
                    print("Current number" + str(self.a.index(str(n)) + 1) + "-----------------------" + self.zentao.get_ele_text(
                        loc2))
                self.zentao.refresh()

            else:
                self.loc.append(self.zentao.get_att(self.loc1, "value"))
                post_code=(self.zentao.get_att(self.loc1, "value"))
                self.zentao.findElement(self.loc1).clear()
                print("Current number" + str(self.a.index(str(n)) + 1) + "----------------------" + post_code)
                continue
        return self.loc

    def write_txt(self):
        post_list=self.test01()
        print(post_list)
        with open("data.txt", "w") as f:
            for line in post_list:
                f.write(line + '\n')
        f.close()


if __name__ == '__main__':
    lianxi().write_txt()
