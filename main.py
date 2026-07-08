import os
##################### Normal Starting Project ######################
from datetime import *
import pandas
import smtplib
import random

today = datetime.now()
today_tuple = (today.month,today.day)

MY_EMAIL = os.environ.get("MY_EMAIL")
MY_PASSWORD = os.environ.get("MY_PASSWORD")

data = pandas.read_csv("birthdays.csv")
data.to_dict()
birthday_dict = {(data_row["month"],data_row["day"]) : data_row for (index,data_row) in data.iterrows()}

names = data["name"].to_list()
files = ["letter_1.txt","letter_2.txt","letter_3.txt"]

if today_tuple in birthday_dict:
        random_file = random.choice(files)
        birthday_person = birthday_dict[today_tuple]
        with open(f"letter_templates/{random_file}", "r") as file:
            read_file = file.read()

        updated_content = read_file.replace("[NAME]",birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(MY_EMAIL, MY_PASSWORD)
            connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=birthday_person["email"],
                    msg=f"Subject: Happy Birthday!!\n\n{updated_content}"
                    )



