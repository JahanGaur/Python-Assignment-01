"""

Python Assignment - 01
Project - Daily Calorie Tracker

Name - Jahan Gaur
Roll Number - 2501730484
Course - B.Tech CSE AI/ML
Section - G
Date - 13-11-2025
"""

import datetime

print("Welcome to your Daily Calorie Tracker! Where you can track your way to a healthy life!")

meal_names = []
calorie_value = []

no_of_meals = int(input("How many meals will you have/had today? "))

for x in range(no_of_meals):
    meal = input("Please enter your meal name. ")
    calorie = float(input(f"Please enter the calorie value for {meal} "))
    meal_names.append(meal)
    calorie_value.append(calorie)

total_calorie = sum(calorie_value)
average_calorie = total_calorie/len(calorie_value)

daily_calorie_limit = float(input("Please enter your daily calorie limit. "))

print(f"Your total calorie limit = {daily_calorie_limit}\nYour total calorie intake today = {total_calorie}\nYour average calorie intake today = {average_calorie}")

if total_calorie <= daily_calorie_limit:
    print("Congratulations! Your calorie intake is within the daily limit today.")
else:
    print(f"Your calorie intake is not within the daily limit today!\nYou comsumed {total_calorie - daily_calorie_limit} calorie more today!")

print("Your Daily Calorie Tracker Summary")
print(f"Meal Name \t Calories")

print(f"---------------------")

for m, c in zip(meal_names, calorie_value):
    print(f"{m} \t\t {c}")

print(f"Total \t {total_calorie}")
print(f"Average \t {average_calorie}")

print(f"---------------------")

save_report = input("Would you like to save the report?\nReply with a Y/N for Yes and No respectively.").lower()

if save_report == "y":
    with open ("calorie_log.txt", "w") as log:
        log.write("Daily Calorie Tracker Summary Log.\n")
        log.write(f"Date & Time = {datetime.datetime.now()}\n")
        log.write("Your Daily Calorie Tracker Summary\n")
        log.write(f"Meal Name \t Calories\n")

        log.write(f"---------------------\n")

        for m, c in zip(meal_names, calorie_value):
            log.write(f"{m} \t\t {c}\n")

        log.write(f"Total \t\t {total_calorie}\n")
        log.write(f"Average \t {average_calorie}\n")

        log.write(f"---------------------\n")
        print("Daily calore tracker report saved to logs.")
else:
    print("Daily calore tracker report not saved to logs.")


