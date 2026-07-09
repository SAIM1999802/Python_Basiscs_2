import requests

# url = "https://api.frankfurter.dev/v2/rates"

# resp = requests.get(url)
# print(resp)
# print(dir(resp))
# print(resp.json())
# print(resp.status_code)
# data = resp.json()
# for item in data:
#     if item["quote"] == "PKR":
#         print(item["rate"])

import requests

# Maslan: ExchangeRate-API ka istemal
url = "https://api.exchangerate-api.com/v4/latest/EUR"
response = requests.get(url)
data = response.json()

amount = 100
rate = data['rates']['PKR']
converted_amount = amount * rate

print(f"{amount} EUR = {converted_amount} PKR")