from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = r"C:\Users\kdrer\Downloads\chromedriver"

driver = webdriver.Chrome(chromedriver)


driver.get('https://www.instagram.com/p/BuE82VfHRa6/')

elems = driver.find_elements_by_xpath("//a[@class='FPmhX notranslate TlrDj']")

users = []

for elem in elems:
    users.append(elem.get_attribute('title'))
    print('Title : ' +elem.get_attribute('title'))

print(users)