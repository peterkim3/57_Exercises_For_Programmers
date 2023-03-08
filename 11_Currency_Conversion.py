d1 = dict(zip(["KOR", "JPN"], [(1323.10, "won"), (137.68, "yen")]))

while True:
    quantity = input(f"How many dollars you exchanging? : ")
    country = input(f"What is the country you want to exchange?: ")

    if quantity.isdigit():
        quantity = int(quantity)
        if quantity <= 0:
            "Wrong input. Try Again."
            continue

    if (exchangeRate := d1.get(country)) == None:
        "Wrong input. Try Again."
        continue
    else:
        break


print(
    f"{quantity} dollars at an exchange rate of \
{exchangeRate[0]} is {round(quantity * exchangeRate[0], 3)} {exchangeRate[1]}"
)


"""
안되누
# https://www.exchangerate-api.com/docs/python-currency-api

import requests

# Where USD is the base currency you want to use
url = "https://v6.exchangerate-api.com/v6/YOUR-API-KEY/latest/USD"

# Making our request
response = requests.get(url)
data = response.json()

# Your JSON object
print(data)
"""

"""
Challenges
clear 1. Build a dictionary of conversion rates and prompt for the countries instead of the rates
2. Wire up your application to an external API that provieds the current exchange rates.
"""
