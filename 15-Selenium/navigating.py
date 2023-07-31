from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chromedriver = r"C:\Users\kdrer\Downloads\chromedriver"

driver = webdriver.Chrome(chromedriver)

url = "https://www.instagram.com/eymenpatik/"
driver.get(url)


time.sleep(15)
