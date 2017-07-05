# -*- coding: utf-8 -*-

from selenium import selenium

#sel = selenium('localhost', 4444, '*firefox', 'http://www.google.com.tw/')
#sel = selenium('localhost', 4444, '*iexplore', 'http://www.google.com.tw/')
sel = selenium('localhost', 4444, '*googlechrome', 'http://www.google.com.tw/')

sel.start()
sel.window_focus()
sel.window_maximize()

sel.open('/')
sel.wait_for_page_to_load(10000)

sel.type("//input[@id='lst-ib']", u'艾小克')
sel.click("//input[@name='btnK']")

assert u'瓶水相逢- 艾小克' == sel.get_text("xpath=(//h3[@class='r']/a)[1]"), 'not match'

sel.stop()