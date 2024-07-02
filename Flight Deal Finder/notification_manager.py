import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from flight_search import FlightSearch

my_email = "aerex0319@gmail.com"
password = "mrkatpwvzvrktvkw"


class NotificationManager:
    def send_notification(self, emails, message):
        # self.message = f"Low Price Alert!\n\nOnly £{price} to fly from {start_city}-{start_airport} to {final_city}-{final_airport}, from {start_date} to {final_date}."

        # msg = MIMEMultipart()
        # msg["From"] = my_email
        # msg["To"] = emails
        # msg["Subject"] = "Flight Price Alert"
        # msg.attach(MIMEText(message, "plain"))
        #
        # try:
        #     with smtplib.SMTP("smtp.gmail.com") as connection:
        #         connection.starttls()
        #         connection.login(user=my_email, password=password)
        #         connection.send_message(msg)
        #         print("Email sent successfully.")
        # except smtplib.SMTPException as e:
        #     print("Error occurred while sending the email:", e)

        # OR
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            for email in emails:
                connection.sendmail(
                    from_addr=my_email,
                    to_addrs=email,
                    msg=f"Subject:New Low Price Flight!\n\n{message}".encode('utf-8')
                )
