# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from selenium import webdriver
from lxml import etree
import time


chrome_path = "C:\Users\P17179\PycharmProjects\Selenium\chromedriver.exe"
web = webdriver.Chrome(chrome_path)
web.maximize_window()


web.get('https://www.pixnet.net/blog/articles/category/19/hot/2')


res = pq(web.find_element_by_xpath("//*").get_attribute("outerHTML"))

print res('.rank-11').find('h3').find('a').text()





web.quit()
#web.close()