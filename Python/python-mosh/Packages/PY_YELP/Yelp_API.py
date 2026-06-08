# what is PYYELP
# PYYELP is Application Programming Interface

import requests
import config

url = "https://api.yelp.com/v3/businesses/search"

headers = {
    "Authorization": "Bearer " + config.api_key
}
params = {
    "term" : "Barber",
    "location": "NYC"
}

response = requests.get(url, headers=headers, params=params)
# we have to send the API key to indicate who we are for authorization
businesses = response.json()["businesses"]
name = [business["name"] for business in businesses if business["rating"] > 4.5]
# list comprehension syntax
print(name)