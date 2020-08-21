from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import requests

import re
import time
import confidential

options = Options()
#headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.92 Safari/537.36'}
headers={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.61 Safari/537.36'}
#search for my user agent on google to get details. Download new version of chromedriver as chrome gets updated
#options.headless = True

#options.add_argument('--no-sandbox')
#chrome_options.add_argument('--headless')

chromedriver="D:\Downloads\chromedrive\chromedriver.exe"
driver=webdriver.Chrome(chromedriver, options=options)
chrome_options = webdriver.ChromeOptions()


#x is 2 to 8
def year_select(x):
    all_orders=driver.find_element_by_xpath('//*[@id="a-autoid-1-announce"]')
    all_orders.click()
    time.sleep(2)

    pathx=f'//*[@id="orderFilter_{x}"]'
    orders20x=driver.find_element_by_xpath(pathx)
    orders20x.click()
    time.sleep(2)



driver.get("https://www.amazon.in")
time.sleep(10)
sign_in=driver.find_element_by_xpath('//*[@id="nav-link-accountList"]')
sign_in.click()
time.sleep(2)
mail_id=driver.find_element_by_xpath('//*[@id="ap_email"]')
mail_id.send_keys(confidential.amazon_mail)
time.sleep(2)
contin=driver.find_element_by_xpath('//*[@id="continue"]')
contin.click()
time.sleep(4)
passw=driver.find_element_by_xpath('//*[@id="ap_password"]')
passw.send_keys(confidential.amazon_pass)

enter_acc=driver.find_element_by_xpath('//*[@id="signInSubmit"]')
enter_acc.click()
time.sleep(10)
my_orders=driver.find_element_by_xpath('//*[@id="nav-orders"]/span[1]')
my_orders.click()
time.sleep(9)

all_orders=driver.find_element_by_xpath('//*[@id="a-autoid-1-announce"]')
all_orders.click()
time.sleep(2)

orders2020=driver.find_element_by_xpath('//*[@id="orderFilter_2"]')
orders2020.click()
time.sleep(2)
i=0
total_price=0.0
flag=0
x=3

while(x<=8):
    for i in range(2,11):
        xpathstr=f'//*[@id="ordersContainer"]/div[{i}]/div[1]/div/div/div/div[1]/div/div[2]/div[2]/span/span'
        if(len(driver.find_elements_by_xpath(xpathstr))<=0):
            flag=1
            break
        item_price=driver.find_element_by_xpath(xpathstr).text
        item_price= item_price.strip()
        item_price = item_price.replace(',','')
        total_price+=float(item_price)
        print(total_price)

    if(flag==1):
        year_select(x)
        x+=1
        flag=0
        print(total_price)
        continue


    if(len(driver.find_elements_by_css_selector('li.a-last > a'))<=0):
        year_select(x)
        print(total_price)
        x+=1
        flag=0

    else:
        nextpg = driver.find_element_by_css_selector('li.a-last > a') .get_attribute('href')

        driver.get(nextpg)
        time.sleep(2)




print(total_price)



driver.quit()
