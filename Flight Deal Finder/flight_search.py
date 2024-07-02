import requests
from flight_data import FlightData
from pprint import pprint

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = "BsjH7h8xcjZqxn2NlX94sJSW3GFzUiPi"


class FlightSearch:
    def get_code(self, name):
        header = {
            "Content-Type": "application/json",
            "Content-Encoding": "gzip",
            "apikey": TEQUILA_API_KEY,
        }

        params = {
            "term": name,
            "location_types": "city",
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/locations/query", params=params, headers=header)
        data = response.json()["locations"]
        code = data[0]["code"]
        return code

    def flights(self, start_city, final_city, from_time, to_time):
        header = {
            "Content-Type": "application/json",
            "Content-Encoding": "gzip",
            "apikey": TEQUILA_API_KEY,
        }

        params = {
            "fly_from": start_city,
            "fly_to": final_city,
            "date_from": from_time.strftime("%d/%m/%Y"),
            "date_to": to_time.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "max_stopovers": 0,
            "curr": "GBP"
        }

        response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", params=params, headers=header)

        try:
            response_data = response.json()["data"]

            if response_data:
                data = response_data[0]
                # flight_data = FlightData(
                #     price=data["price"],
                #     start_city=data["route"][0]["cityFrom"],
                #     start_airport=data["route"][0]["flyFrom"],
                #     final_city=data["route"][1]["cityTo"],
                #     final_airport=data["route"][1]["flyTo"],
                #     start_date=data["route"][0]["local_departure"].split("T")[0],
                #     final_date=data["route"][2]["local_departure"].split("T")[0],
                #     stop_overs=1,
                #     via_city=data["route"][0]["cityTo"]
                # )
                #
                # return flight_data
            else:
                return None

        except IndexError:
            params["max_stopovers"] = 1
            response = requests.get(url=f"{TEQUILA_ENDPOINT}/v2/search", headers=header, params=params)

            response_data = response.json()["data"]
            # pprint(data)
            if response_data:
                data = response_data[0]
                flight_data = FlightData(
                    price=data["price"],
                    start_city=data["route"][0]["cityFrom"],
                    start_airport=data["route"][0]["flyFrom"],
                    final_city=data["route"][1]["cityTo"],
                    final_airport=data["route"][1]["flyTo"],
                    start_date=data["route"][0]["local_departure"].split("T")[0],
                    final_date=data["route"][2]["local_departure"].split("T")[0],
                    stop_overs=1,
                    via_city=data["route"][0]["cityTo"]
                )

                return flight_data
            else:
                return None
        else:
            flight_data = FlightData(
                price=data["price"],
                start_city=data["route"][0]["cityFrom"],
                start_airport=data["route"][0]["flyFrom"],
                final_city=data["route"][0]["cityTo"],
                final_airport=data["route"][0]["flyTo"],
                start_date=data["route"][0]["local_departure"].split("T")[0],
                final_date=data["route"][1]["local_departure"].split("T")[0],
            )

            return flight_data
