from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path  = Service("C:\Development\chromedriver.exe")
options  = webdriver.ChromeOptions()

driver = webdriver.Chrome(service=chrome_driver_path,options=options)
driver.get(url="http://orteil.dashnet.org/experiments/cookie/")
cookie_click = driver.find_element(By.ID, "cookie")
timeout = time.time() + 5
five_min = time.time() + 300

upgrade_ids = driver.find_elements(By.CSS_SELECTOR,"#store div")
upgradesids_list = [item.get_attribute("id") for item in upgrade_ids]


while True:
    cookie_click.click()
    if time.time() > timeout:

        items_cost = driver.find_elements(By.CSS_SELECTOR, "#store b")
        prices = []
        for item in items_cost[:8]:
            item_text = item.text
            if item_text != "":
                cost = int(item_text.split("-")[1].strip().replace(',',''))
                prices.append(cost)

        items_dict = {}

        for n in range(len(prices)):
            items_dict[prices[n]] = upgradesids_list[n]

        money = driver.find_element(By.ID,"money")
        money_count = money.text
        if ',' in money_count:
            money_count = money_count.replace(',','')
        cookie_count = int(money_count)

        present_expensive = {}
        for cost, id in items_dict.items():
            if cookie_count > cost:
                present_expensive[cost] = id

        highest_price_buy = max(present_expensive)
        print(f"max :{highest_price_buy}")
        purchase_id = present_expensive[highest_price_buy]

        driver.find_element(By.ID, purchase_id).click()
        timeout = time.time() + 5
    if time.time() > five_min:
        cookies_all =  driver.find_element(By.ID, "cps").text
        print(f"cookie: {cookies_all}")
        break


# while True:
#     cookie_click.click()
#     if time.time() > timeout:
#         for up in upgrades:
#             up.click()
#

