import requests
from pprint import pprint

PRICES_SHEETY_ENDPOINT = "https://api.sheety.co/c66f910988a4ff3e72e325581e147ebb/flightDeals/prices"
USERS_SHHETY_ENDPOINT = "https://api.sheety.co/c66f910988a4ff3e72e325581e147ebb/flightDeals/users"

sheety_header = {
            "Authorization": "Basic YWVyZXg6QWxpZUAxMjM0NTY=",
            "Content-Type": "application/json",
        }

class DataManager:
    def __init__(self):
        self.price_list = []
        self.customer_data = []

    def price(self):
        response = requests.get(url=PRICES_SHEETY_ENDPOINT, headers=sheety_header)
        data = response.json()
        self.price_list = data["prices"]
        return self.price_list

    def city_code(self):
        for city in self.price_list:
            code_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }

            response = requests.put(url=f"{PRICES_SHEETY_ENDPOINT}/{city['id']}", json=code_data, headers=sheety_header)

    def enter_data(self, f_name, l_name, email):
        get_response = requests.get(url=USERS_SHHETY_ENDPOINT)

        code_data = {
            "user": {
                "firstName": f_name,
                "lastName": l_name,
                "email": email,
            }
        }

        response = requests.post(url=USERS_SHHETY_ENDPOINT, json=code_data, headers=sheety_header)

    def customer_email(self):
        response = requests.get(url=USERS_SHHETY_ENDPOINT, headers=sheety_header)
        data = response.json()
        self.customer_data = data["users"]
        return self.customer_data
