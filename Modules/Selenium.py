
#pip install -m pip install selenium

#selenium requires a chrome driver that can be found here:
#https://sites.google.com/a/chromium.org/chromedriver/downloads

# this bit of code will open the chrome browser and go google.com
from selenium import webdriver
browser = webdriver.Chrome('G:\Software\Python\Lib\site-packages\selenium\chromedriver') # path to chromedriver.exe
browser.get("https://www.google.com/")