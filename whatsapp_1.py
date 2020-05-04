import csv
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

dates = []
scores = []

driver =  webdriver.Chrome()
driver.get("https://web.whatsapp.com/")
time.sleep(5) 
with open('/home/sid/Desktop/whatsapp/whatsapp.csv') as csvDataFile:
    csvReader = csv.reader(csvDataFile)
    for row in csvReader:
        dates.append(row[0])
        scores.append(row[1])
a=len(dates)

for x in range(a):
  link = str("https://web.whatsapp.com/send?phone=91")+dates[x]
  driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't')
  driver.get(link)
  time.sleep(10) 

#select the message and send it
  msg_box = driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[2]/div/div[2]")
  msg_box.send_keys(scores[x])
  driver.find_element_by_xpath("//*[@id='main']/footer/div[1]/div[3]/button").click()
  print("Success for "+dates[x])
  time.sleep(10) 
driver.close()


