import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

my_email = "aerex0319@gmail.com"
password = "mrkatpwvzvrktvkw"

optimal_price = 100;
url="https://www.amazon.com/dp/B075CYMYK6?ref_=cm_sw_r_cp_ud_ct_FM9M699VKHTT47YD50Q6&th=1"

header = {
    "Accept-Language": "en-US,en;q=0.9",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36",
}

response = requests.get(url=url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(class_="a-offscreen").getText()
price_only = float(price.split("$")[1])
product = soup.find(id="productTitle").getText().strip()

if price_only<optimal_price:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="choprakaran3008@gmail.com",
            msg=f"Subject:Low price available for you.\n\nHurry!\n{product} is now at {price}.\n\nHere's the link:\n{url}".encode('utf-8')
        )
