#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2020/4/14 17:39
# @Author  : afanti
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import NoAlertPresentException
from datetime import datetime
from time import sleep
import random
import os


uname = '' #帐号
pswd = '' #密码
qesnum =  # 安全提问 参考下面
qan = ''.decode("utf8","ignore") # 安全提问答案
# signtime = "09:30" # 每日签到时间

# 0 = 没有安全提问
# 1 = 母亲的名字
# 2 = 爷爷的名字
# 3 = 父亲出生的城市
# 4 = 您其中一位老师的名字
# 5 = 您个人计算机的型号
# 6 = 您最喜欢的餐馆名称
# 7 = 驾驶执照的最后四位数字

qesarr = ['母亲的名字','爷爷的名字','父亲出生的城市','您其中一位老师的名字','您个人计算机的型号','您最喜欢的餐馆名称','驾驶执照的最后四位数字']
user_agent = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.50 Safari/537.36'



options = webdriver.ChromeOptions()
options.add_argument('lang=zh_CN.UTF-8')
options.add_argument('user-agent={user_agent}')
options.add_argument('log-level=3') # LOG 回报等级
options.add_argument('--headless') # 无头模式
options.add_argument('--disable-gpu') # windows不加会跳gpu错 但不影响功能
options.add_argument('disable-infobars')

chromedriver = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
os.environ["webdriver.chrome.driver"] = chromedriver

driver = webdriver.Chrome(chromedriver,chrome_options=options)
driver.implicitly_wait(30)
driver.set_window_size(1600, 900) # 视窗大小 太小抓不到登入按钮
driver.get("https://www.t00ls.net/login.html")
driver.find_element_by_id("username").send_keys(uname)
driver.find_element_by_id("password").send_keys(pswd)

if(qesnum != 0):
	Select(driver.find_element_by_id("questionid")).select_by_visible_text(qesarr[qesnum-1])
	driver.find_element_by_id("questionid").click()
	driver.find_element_by_id("answer").send_keys(qan)

driver.find_element_by_name("loginsubmit").click()




while True:

    try:
        driver.get("https://www.t00ls.net/index.php")
        sleep(random.randrange(30,100))
        driver.find_element_by_link_text(u"技术交流讨论(Technical Discussions)").click()
        print "Technical Discussions....."
        sleep(random.randrange(30,100))
        driver.find_element_by_link_text(u"返回首页").click()
        print "Retern index......"
        sleep(random.randrange(30,100))
    except KeyboardInterrupt:
        print ("使用者停止程式...!")
        break
    except:
        sleep(300)

driver.quit()

# 总积分计算公式: 总积分=TCV*2+主题数+精华帖数*2+发帖数*0.2+在线时间(小时)*0.1
