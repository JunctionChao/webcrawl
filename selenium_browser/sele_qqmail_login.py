# -*- encoding: utf-8 -*-

from selenium import webdriver
import time


driver = webdriver.Chrome()
driver.get("https://mail.qq.com/")

# 由于qq邮箱登录元素是在一个iframe中，不能直接定位元素
# iframe相当于嵌套的另一个页面，需要切换的iframe
driver.switch_to.frame("login_frame")


driver.find_element_by_id("u").send_keys('324356546')


time.sleep(3)
driver.close()