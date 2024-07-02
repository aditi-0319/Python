import requests
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

my_email = "aerex0319@gmail.com"
password = "mrkatpwvzvrktvkw"
subject = ""

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
NEWS_COMPANY_NAME = "tesla"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API_KEY = "U8617AUB84JX6RS1"

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API_KEY = "cce7775b34364d129c3241647727e053"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API_KEY,
}

response_stock = requests.get(STOCK_ENDPOINT, params=stock_params)
response_stock.raise_for_status()
data = response_stock.json()["Time Series (Daily)"]

data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = float(yesterday_data["4. close"])

day_before_yesterday_data = data_list[1]
day_before_yesterday_closing_price = float(day_before_yesterday_data["4. close"])

if yesterday_closing_price > day_before_yesterday_closing_price:
    symbol = "🔺"
else:
    symbol = "🔻"

positive_difference = abs(yesterday_closing_price-day_before_yesterday_closing_price)
percentage_difference = round((positive_difference/yesterday_closing_price) * 100, 4)

news_params = {
    "q": NEWS_COMPANY_NAME,
    "apiKey": NEWS_API_KEY,
}

response_news = requests.get(NEWS_ENDPOINT, params=news_params)
response_news.raise_for_status()
news = response_news.json()["articles"]


def send_email(subject, body):
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = "rosychopra1971@gmail.com"
    msg['Subject'] = subject

    msg.attach(MIMEText(body, 'plain'))

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="rosychopra1971@gmail.com",
            msg=msg.as_string()
        )


def get_news():
    global subject
    latest_news_title = []
    latest_news_description = []
    for n in range(3):
        title = news[n]["title"]
        description = news[n]["description"]
        latest_news_title.append(title)
        latest_news_description.append(description)

        # with smtplib.SMTP("smtp.gmail.com") as connection:
        #     connection.starttls()
        #     connection.login(user=my_email, password=password)
        #     connection.sendmail(
        #         from_addr=my_email,
        #         to_addrs="rosychopra1971@gmail.com",
        #         msg=f"Subject:Tesla Stack News\n\n{STOCK_NAME} : {percentage_difference}% {status}\nHeadline : {encoded_titles}\nBrief : {encoded_descriptions}"
        #     )

        msg = MIMEMultipart()
        msg['From'] = my_email
        msg['To'] = "rosychopra1971@gmail.com"
        msg['Subject'] = "Tesla Stock News"

        for title, description in zip(latest_news_title, latest_news_description):
            subject = "Tesla Stock News"
            body = f"{STOCK_NAME} : {symbol}{percentage_difference}%\n\nHeadlines:\n{title}\n\nBrief:\n{description}"

        send_email(subject, body)


if percentage_difference > 5:
    get_news()



















    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]

#TODO 2. - Get the day before yesterday's closing stock price

#TODO 3. - Find the positive difference between 1 and 2. e.g. 40 - 20 = -20, but the positive difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.asp

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.

#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").

    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

