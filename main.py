import requests
import os
from twilio.rest import Client

account_sid = os.getenv("ACCOUNT_SID")
auth_token = os.getenv("AUTH_TOKEN")
API_KEY = os.getenv("OWM_API_KEY")
print(account_sid,auth_token,API_KEY)
# print(API_KEY)
LAT = 28.404289
LON = 77.290321
#OEM_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat" : LAT,
    "lon" : LON,
    "appid" : API_KEY,
    "cnt" : 4,
}

response = requests.get(OEM_ENDPOINT,params=weather_params)
response.raise_for_status()
data = response.json()

# print(f"Status Code : {data["cod"]}")
# print(f"Response : {data}")
will_rain = False
for forecast in data["list"]:
    condition_code = forecast["weather"][0]["id"] 
    if condition_code < 700:
        will_rain = True
#if will_rain:
#    client = Client(account_sid, auth_token)
#    message = client.messages.create(
#        to="+919582400091",
#        from_="+17372508034",
#        body="sms_event_notifications",
#    )

    print(message.body)

    
    
