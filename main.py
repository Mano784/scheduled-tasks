##################### Normal Starting Project ######################
from datetime import *
import pandas
import smtplib
import random
my_email = "manonith308@gmail.com"
password = "xxsn iyje xcnf cnxt"
today = datetime.now()
today_tuple = (today.month,today.day)

data = pandas.read_csv("birthdays.csv")
data.to_dict()
birthday_dict = {(data_row["month"],data_row["day"]) : data_row for (index,data_row) in data.iterrows()}

names = data["name"].to_list()
files = ["letter_1.txt","letter_2.txt","letter_3.txt"]
random_file = random.choice(files)
for _ in range(5):
    if today_tuple in birthday_dict:
        birthday_person = birthday_dict[today_tuple]
        with open(f"letter_templates/{random_file}", "r") as file:
            read_file = file.read()

        updated_content = read_file.replace("[NAME]",birthday_person["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(my_email,password)
            connection.sendmail(from_addr = my_email,to_addrs = birthday_person["email"],
                                 msg = f"Subject: Happy Birthday!!\n\n{updated_content}")




