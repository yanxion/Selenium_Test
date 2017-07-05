# -*- coding: utf-8 -*-
from pyquery import PyQuery as pq
from selenium import webdriver
from lxml import etree
import time


chrome_path = "C:\Users\P17179\PycharmProjects\Selenium\chromedriver.exe"
web = webdriver.Chrome(chrome_path)

web.get('https://www.pixnet.net/blog/articles/category/19/hot/2')

#print web.page_source
#res = pq(web.page_source)


res = pq( 'https://www.pixnet.net/blog/articles/category/19/hot/2', encoding="utf-8")

print res
time.sleep(5)
#print res('li.rank-11').find('h3').find('a').text()


#web.find_element_by_link_text(u"下一頁").click()
web.close()