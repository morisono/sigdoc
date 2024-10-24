# coding: utf-8

from selenium import webdriver
import re

asins=[]

driver = webdriver.PhantomJS()

for page in range(1,3):
    url = "http://www.amazon.co.jp/s/?node=2277721051&field-enc-merchantbin=AN1VRQENFRJN5&page=%s" % page
    driver.get(url)
    elems = driver.find_elements_by_css_selector("ul#s-results-list-atf li")

    for e in elems:
        asin = {}
        if e.get_attribute("data-asin"):
            try:
                text =  e.find_element_by_xpath(".//span[contains(text(), '%s')]" % "発売予定").text
                release_date = re.search(u"[0-9]{4}/[0-9]{1,2}/[0-9]{1,2}", text)
                asin["asin"]  = e.get_attribute("data-asin")
                asin["title"] =  e.find_element_by_tag_name("h2").text
                asin["release_data"] =  release_date.group()
                print asin
            except:
                pass
    
driver.quit()