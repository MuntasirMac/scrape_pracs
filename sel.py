# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
import time

# option = webdriver.ChromeOptions()
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=option)

from undetected_chromedriver import Chrome

chrome = Chrome()

chrome.get('https://www.ryans.com/category/laptop-all-laptop?limit=100&sort=D&osp=1&st=0')
# time.sleep(20)
chrome.find_element('xpath', '//a[@rel="next"]').click()

input("Press Enter to close the window")
chrome.quit()