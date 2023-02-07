import pprint
import requests

address = "OIJASOIFHSPOIFHASIOFHPAOSIHFPIASHFPIASH"

print(requests.get(f"https://public-sdc.trendyol.com/discovery-web-websfxgeolocation-santral/geocode",
                   params={"address": address}).json())
