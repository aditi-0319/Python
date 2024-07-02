from selenium import webdriver
from selenium.webdriver.common.by import By
import time

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://orteil.dashnet.org/experiments/cookie/")

cookie = driver.find_element(By.ID, value="cookie")

items = []
item_id = []
price = driver.find_elements(By.CSS_SELECTOR, value="#store div b")
item = driver.find_elements(By.CSS_SELECTOR, value="#store div")
for n in price:
    if n.text != "":
        m = int(n.text.split("-")[1].strip().replace(",", ""))
        items.append(m)

for n in item:
    if n.text != "":
        m = n.get_attribute("id")
        item_id.append(m)

sec_time = time.time() + 5
min_time = time.time() + 60*5

while True:
    cookie.click()

    if time.time() > sec_time:
        money = int(driver.find_element(By.ID, value="money").text.replace(",", ""))

        available_items = []
        available_items_id = []
        for n in items:
            if n <= money:
                available_items.append(n)
                n_index = available_items.index(n)
                available_items_id.append(item_id[n_index])

        buy_item = max(available_items)
        buy_item_index = available_items.index(buy_item)
        buy_item_id = available_items_id[buy_item_index]

        bought_item = driver.find_element(By.ID, value=buy_item_id)
        bought_item.click()

        sec_time = time.time() + 5

    if time.time() > min_time:
        cookie_per_sec = driver.find_element(By.ID, value="cps")
        print(cookie_per_sec.text)
        break


