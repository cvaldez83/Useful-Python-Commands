from selenium import webdriver

from selenium import webdriver
browser = webdriver.Chrome('G:\Software\Python\Lib\site-packages\selenium\chromedriver') # path to chromedriver.exe
browser.get("https://automatetheboringstuff.com")

elem = browser.find_element_by_css_selector('body > div.main > div:nth-child(1) > ul:nth-child(18) > li:nth-child(1) > a')
elem.click()

elems = browser.find_elements_by_css_selector('p')
print('length is ' + str(len(elems)))

for i in elems:
    print(i)

#to click on a search box:

#sudo code -> searchElem = browser.find_element_by_css_selector('whatever_the_selector_is')