import requests
from datetime import datetime

MY_LAT = 30.07834
MY_LNG = -107.14663

parameters = {
    'lat': MY_LAT,
    'lng': MY_LNG,
    'formatted': 0,

}


response = requests.get('https://api.sunrise-sunset.org/json', params=parameters)
response.raise_for_status()
data = response.json()
print(data)

sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

time_now = datetime.now()

print(sunrise)
print(sunset)
print(time_now.hour)