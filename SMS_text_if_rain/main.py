import requests
from twilio.rest import Client

SF_LAT = 37.774929
SF_LONG = -122.419418

# get both values from open weather map website
api_key = "Your api key"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/onecall"

# get both values from twilio website
account_sid = "Your account_sid"
auth_token = "Your auth_token"

parameter = {
    "lat": SF_LAT,
    "lon": SF_LONG,
    "exclude": "current,minutely,daily",
    "appid": api_key,
}


response = requests.get(OWM_endpoint, params=parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Bring an ☂️",
        from_= "Your Twilio phone number",
        to="Your cell phone number"
        )
    
print(message.status)