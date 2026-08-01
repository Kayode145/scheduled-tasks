##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import os
import smtplib
import  pandas
import random
import datetime as dt

EMAIL = os.environ.get("mjude14589@gmail.com")
PASSWORD = os.environ.get("hpxxggcxefvlwzga")


birthday_data = pandas.read_csv("birthdays.csv")

date = dt.datetime
day = date.now().day
month = date.now().month

for index,row in birthday_data.iterrows():
    if row["day"] == day:
        file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
        with open(file_path) as data:
            letter = data.read()
            letter_to_send = letter.replace("[NAME]", row["name"])
        with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
            connection.starttls()
            connection.login(user=EMAIL,password=PASSWORD)
            connection.sendmail(
                from_addr=EMAIL,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday!\n\n{letter_to_send}"
            )
