from datetime import datetime, timedelta
from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager
import requests

# from pprint import pprint

data_manager = DataManager()
price_list = data_manager.price()
flight_search = FlightSearch()
notification_manager = NotificationManager()

ORIGIN = "LON"

# print("Welcome to the Flight Club!\nWe find the best flight deals and email you regarding them.")
# f_name = input("Enter your first name : ").title()
# l_name = input("Enter your last name : ").title()
# email = ""
# r_email = " "
#
# while email != r_email:
#     email = input("Enter your email : ")
#     if email.lower() == "exit":
#         exit()
#     r_email = input("Enter your email again : ")
#
#     if r_email.lower() == "exit":
#         exit()
#
# print("\nYou are in the club!\n")
# data_manager.enter_data(f_name, l_name, email)

if price_list[0]["iataCode"] == "":
    for location in price_list:
        from flight_search import FlightSearch

        flight_search = FlightSearch()

        location["iataCode"] = flight_search.get_code(location["city"])

        data_manager.city_code()

tomorrow = datetime.now() + timedelta(days=1)
six_months = datetime.now() + timedelta(days=(6 * 30))

for location in price_list:
    flight = flight_search.flights(ORIGIN, location["iataCode"], from_time=tomorrow, to_time=six_months)

    if flight is None:
        continue

    if flight.price < location["lowestPrice"]:
        user = data_manager.customer_email()
        emails = [row["email"] for row in user]
        name = [row["firstName"] for row in user]

        message = f"Low Price Alert!\n\nOnly £{flight.price} to fly from {flight.start_city}-{flight.start_airport} to {flight.final_city}-{flight.final_airport}, from {flight.start_date} to {flight.final_date}."

        if flight.stop_overs > 0:
            message += f"\nFlight has {flight.stop_overs} stop over, via {flight.via_city}."

        notification_manager.send_notification(emails, message)
                # flight.price,
                # flight.start_city,
                # flight.start_airport,
                # flight.final_city,
                # flight.final_airport,
                # flight.start_date,
                # flight.final_date
