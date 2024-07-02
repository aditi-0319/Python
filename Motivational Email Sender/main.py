import smtplib
import random
import datetime as dt

with open("quotes.txt") as file:
    quote_list = file.readlines()

new_list = []
for n in quote_list:
    new_list.append(n.replace("\n", ""))

quote = random.choice(new_list)

now = dt.datetime.now()
day = now.weekday()

if day == 3:
    print(quote)

my_email = "aerex0319@gmail.com"
password = "mrkatpwvzvrktvkw"

with smtplib.SMTP("smtp.gmail.com") as connection:
    connection.starttls()
    connection.login(user=my_email, password=password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="rosychopra1971@gmail.com",
        msg=f"Subject:Quote of the day\n\n{quote}"
    )
