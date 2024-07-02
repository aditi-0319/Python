import requests

response_code = [200, 201, 202, 203, 204, 205, 206, 207, 208, 226]
delete_id = 3
update_id = 1

url = "http://localhost:5000"

post = {
    "name": "John F. Kennedy",
    "quote": "Life is never easy. There is work to be done and obligations to be met – obligations to truth, to justice, and to liberty.",
}

put = {
    "name": "Thomas A. Edison",
}

response = requests.get(url=f"{url}/get")
if response.status_code in response_code:
    print(response.text)
else:
    print(f"Get request failed with status code: {response.status_code}")
    print(response.json())


# response = requests.post(url=f"{url}/add", json=post)
# if response.status_code in response_code:
#     print(f"Post request successful! Status Code: {response.status_code}")
#     print(response.json())
# else:
#     print(f"Post request failed with status code: {response.status_code}")
#     print(response.json())


# response = requests.put(url=f"{url}/put/{update_id}", json=put)
# if response.status_code in response_code:
#     print(f"Put request successful! Status Code: {response.status_code}")
#     print(response.json())
# else:
#     print(f"Put request failed with status code: {response.status_code}")
#     print(response.json())


# response = requests.delete(url=f"{url}/delete/{delete_id}")
# if response.status_code in response_code:
#     print(f"Delete request successful! Status Code: {response.status_code}")
#     print(response.json())
# else:
#     print(f"Delete request failed with status code: {response.status_code}")
#     print(response.json())
