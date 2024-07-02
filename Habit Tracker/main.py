import requests
import datetime as dt

USERNAME = "aerex"
TOKEN = "lsf73f648fs48fs68f5efy435"
GRAPH_ID = "graph1"

PIXELA_ENDPOINT = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=PIXELA_ENDPOINT, json=user_params)

GRAPH_ENDPOINT = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs"

graph_params = {
    "id": "graph1",
    "name": "Work Graph",
    "unit": "Hours",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

pixel_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}"

today = dt.datetime(year=2023, month=8, day=2)

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours of work did you do?\n")
    # OR
    # "quantity": "12.5",
}

response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)

update_params = {
    "quantity": "5.5",
}

update_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.put(url=update_endpoint, json=update_params, headers=headers)

delete_endpoint = f"{PIXELA_ENDPOINT}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"
# response = requests.delete(url=delete_endpoint, headers=headers)
print(response.text)
