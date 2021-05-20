import requests
import os

sky_scanner_endpoint = "skyscanner-skyscanner-flight-search-v1.p.rapidapi.com"
sky_scanner_key = os.getenv("SKY_SCANNER_KEY")

headers = {
    'x-rapidapi-key': sky_scanner_key,
    'x-rapidapi-host': sky_scanner_endpoint,
}

# Used in some Skyscanner APIs
params = {
    "inboundpartialdate": "2019-01-02",
}

link_params = {
    "country": "US",
    "currency": "USD",
    "locale": "en-US",
    "destinationplace": "SFO-sky",
    "originplace": "ORD-sky",
    "outboundpartialdate": "2021-09-01",
    "inboundpartialdate": "2021-09-05",
}

path = "https://" + sky_scanner_endpoint + "/apiservices/browsequotes/v1.0"

for _ in link_params.values():
    if _ != "":
        path += "/" + _

response = requests.get(path, headers=headers)
response.raise_for_status()
print(response.text)
