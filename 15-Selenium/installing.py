from selenium import webdriver

chromedriver = r"C:\Users\kdrer\Downloads\chromedriver"

driver = webdriver.Chrome(chromedriver)
driver.get("https://www.youtube.com/watch?v=eDrFWRi13DY")