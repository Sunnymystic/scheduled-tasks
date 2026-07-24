##################### Extra Hard Starting Project ######################

import smtplib
import datetime as dt
import random as rd
import pandas as pd
import os

now = dt.datetime.now()
day = now.day
month = now.month
year = now.year
# AFTER (secrets stored securely in GitHub)
MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")
to_address = ""

print(year, month, day)

data = pd.read_csv("birthdays.csv")
data_list = data.to_dict(orient="records")

for item in data_list:
    if item["day"] == day and item["month"] == month:
        name = item["name"]
        to_address = item["email"]
        letters = ["letter_templates/letter_1.txt","letter_templates/letter_2.txt","letter_templates/letter_3.txt"]
        selected_format = rd.choice(letters)
        with open(selected_format,"r") as f:
            content = f.readlines()
            content[0] = content[0].replace("[NAME]",name)
            actual_content = " ".join(content)
            MY_EMAIL = "iamdogra007@gmail.com"
        with smtplib.SMTP("smtp.gmail.com",587) as connection:  # Build connection
            connection.starttls()                       # Secure connection
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAILl,
                to_addrs=to_address,
                msg=f"Subject:Birthday Wishes\n\n{actual_content}"
        )
            



