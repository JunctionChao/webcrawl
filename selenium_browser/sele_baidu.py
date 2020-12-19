# -*- encoding: utf-8 -*-

from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException

driver = webdriver.Chrome()
# PhantomJS 无界面的内存浏览器
# driver = webdriver.PhantomJS(executable_path=r'D:\Software\phantomjs-2.1.1-windows\bin\phantomjs.exe')

# 设置窗口大小
driver.set_window_size(1440, 900)

driver.get("http://www.baidu.com")

# 进行截屏
# driver.save_screenshot("./baidu.png")

# 元素定位
driver.find_element_by_id("kw").send_keys('python')
driver.find_element_by_id("su").click()

# driver获取cookie
# cookies = driver.get_cookies()
# print(cookies)
# print("--"*50)
# cookies = {i['name']: i['value'] for i in cookies}
# print(cookies)

# dirver获取html页面
# print(driver.page_source) # 浏览器中elements的内容(包括js等请求后的页面)


# 显式等待元素
try:
    element = WebDriverWait(driver, 1).until(
        EC.presence_of_element_located((By.LINK_TEXT, "下一页 >"))
    )
except NoSuchElementException as e:
    print("Error: ", e.args)
else: # 没触发异常
    print(element.get_attribute("href"))
    # 获取下一页的地址
    print(driver.find_element_by_link_text("下一页 >").get_attribute("href"))
    print(driver.find_element_by_partial_link_text("下一页").get_attribute("href"))


time.sleep(3)
# 关闭当前页面
driver.close()

