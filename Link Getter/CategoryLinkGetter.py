import requests
import csv
import pandas
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import os
import time

options = Options()
options.add_argument("--headless --window-size=1920,1200")

driver = webdriver.Chrome('chromedriver.exe')
main_url = "https://www.nba.com/stats/teams/traditional?sort=W_PCT&dir=-1&Season=2014-15"

driver.get(main_url)
time.sleep(5)

html = driver.page_source
soup = BeautifulSoup(html, "html.parser")
all_data = soup.find_all('a', attrs={'data-track' : 'video'})




with open('CategoryLinks.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['links'])
    for i in range(len(all_data)):
        writer.writerow([all_data[i]['href']])