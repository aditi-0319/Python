import pandas
import datetime as dt
import random
import smtplib

my_email = "aerex0319@gmail.com"
password = "mrkatpwvzvrktvkw"

now = dt.datetime.now()
today_month = now.month
today_day = now.day
today = (today_month, today_day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

if today in birthdays_dict:
    file_path = f"./letter_templates/letter_{random.randint(1, 3)}.txt"

    with open(file_path) as file:
        letter = file.read()
        new_letter = letter.replace("[NAME]", birthdays_dict[today]["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs=birthdays_dict[today]["email"],
                msg=f"Subject: Happy Birthday!\n\n{new_letter}"
            )
