import requests
from datetime import datetime
import time as ti
import smtplib

MY_LAT = 56.234812  # Your latitude
MY_LONG = 43.458755  # Your longitude
MY_EMAIL = "safetymysecondnamefirstabsence@gmail.com"
MY_PASSWORD = "*+1u*6xKN6$$48T"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


def iss_ahead():
    return -5 <= MY_LONG - iss_longitude <= 5 and -5 <= MY_LAT - iss_latitude <= 5


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data1 = response.json()
sunrise = int(data1["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data1["results"]["sunset"].split("T")[1].split(":")[0])

time_now = str(datetime.now())
now = time_now.split(":")[0].split(" ")[-1]

is_on = True
while is_on:
    if iss_ahead():
        print("hui")
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs="chesnokovaleks001@gmail.com",
                msg="Subject:Rise your eyes!\n\nISS is ahead")
    ti.sleep(60)
