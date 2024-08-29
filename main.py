import requests
from datetime import datetime

MY_LAT = 28.950378  # Your latitude
MY_LONG = -13.744839  # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    # data = response.json()
    data = {'timestamp': 1724491289, 'message': 'success',
            'iss_position': {'latitude': '24.7221', 'longitude': '-16.2934'}}
    print(data)

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    if MY_LAT - 5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        print("True!")
        return True

def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    hour_now = datetime.now().hour
    if sunset >= hour_now <= sunrise:
        print("it's night")
        return True


if is_iss_overhead() and is_night():

    #send e-mail
    print("ISS Overhead")
else:
    print("it isn't night time!")
# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
