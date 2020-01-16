#coding:utf-8
import time
from selenium import webdriver
aa=webdriver.Chrome()
aa.get("http://www.baidu.com")
try:
 ab=aa.find_element_by_link_text("新闻")
 ab.click()
 time.sleep(3)
 aa.back()
 time.sleep(3)
 aa.forward()
 print ("test pass:refesh")
except Exception as e:
   print("exception",format(e))
