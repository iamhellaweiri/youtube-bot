import time
import random
from selenium import webdriver

driver = webdriver.Chrome('D:\pythoninstaller\chromedriver_win32\chromedriver.exe')

sleep_time = 0

for i in range(1000):
    print("Watcing for {} time".format(i))
    driver.get("https://www.youtube.com/watch?v=pOS3gN4Sgig&t=2s")
    time.sleep(sleep_time) # Let the user actually see something!
    sleep_time = (20)

time.sleep(5) # Let the user actually see something!
driver.quit()
