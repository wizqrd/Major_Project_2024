# This is my Stock Simulator Major
# Scrapes data from yahoo finance allowing for real time stock price simulation
# Portfolio has 25000$ to start with

# Imports
import csv  # I've used import csv to format my stock prices
import os.path  # I am using import os path for checking if a file exists, getting the absolute path of a file.
import webbrowser  # Using this for displaying my web based documents, hoping to use it for yahoo finance
from datetime import datetime, date, timedelta  # This was recommended to me for easily managing my dates and times

import datetime
import bcrypt
import matplotlib.pyplot as plt  # Hoping this will allow me to display graphs of the price going up and down
import pandas as pd  # For managing my 2-d and 1-d data
import requests  # This is used, so I don't have to add query requests at the end of yahoo URL
import yfinance as yf  #
from bs4 import BeautifulSoup  #

# I'm using a csv file to store data for usernames
# If the file exists, it will read the file to get the usernames and corresponding passwords

with open('user_info.csv', 'a', newline='') as csvfile:
    headers = ['Date of Account Creation', 'Time of Account Creation', 'Username', 'Password']
    writer = csv.DictWriter(csvfile, delimiter=',', fieldnames=headers)
    writer.writeheader() if not os.path.isfile('user_info.csv') else None

# Made a script that will store data on a CSV file when a user logs in

def check_username_availability(username):
    """Checks if the username is already taken."""
    usernames_df = pd.read_csv("user_info.csv")
    return username not in usernames_df["Username"].tolist()


def create_account(username, password):
    """Creates a new user account."""
    moment = datetime.datetime.now()
    datenow = moment.strftime("%d/%m/%y")
    timenow = moment.strftime("%H:%M")

    with open("user_info.csv", "a", newline="") as file_pointer:
        csv_pointer = csv.writer(file_pointer)
        hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        row = [datenow, timenow, username, hashed_password]
        csv_pointer.writerow(row)
    print("Your account has been successfully created!")


def get_secure_password():
    while True:
        password = input("Please choose a secure password for this account: ")
        confirm_password = input("Please confirm your password: ")
        if password != confirm_password:
            print("Passwords don't match. Please try again.")
            continue
        return password


def validate_username(username):
    """Validates the username format and checks for availability."""
    if username.upper() == "B":
        return None
    if len(username) < 4:
        print("Please enter a minimum of 4 characters!")
        return None
    if not check_username_availability(username):
        print("Sorry, that username is already taken. Please choose a different one.")
        return None
    return username


def login():
    """Handles the login process."""
    username_login = input("Please enter your username (or B to go back): ")
    if username_login.upper() == "B":
        return None

    try:
        usernames_df = pd.read_csv("user_info.csv")
        list_of_usernames = usernames_df["Username"].tolist()
        list_of_passwords = usernames_df["Password"].tolist()

        if username_login not in list_of_usernames:
            print("That username was not found. Please try again!")
            return None

        password_login = input(f"Welcome back {username_login}! Please enter your password: ")

        hashed_password = list_of_passwords[list_of_usernames.index(username_login)]
        if bcrypt.checkpw(password_login.encode("utf-8"), hashed_password.encode("utf-8")):
            print("Your password matches! Welcome")
            # You can add code to proceed with the simulation here
            return True
        else:
            print("Your entered password is incorrect, please try again")
            return None

    except Exception as e:
        print("An error occurred:", e)
        return None


def main():
    """Main loop for user interaction."""
    while True:
        try:
            account_choice = input("""
Hello! Welcome to the stock simulator!
[L] - Log In
[S] - Sign Up: """).upper()

            if account_choice == "S":
                username = validate_username(input("Enter your desired username (min 4 characters): "))
                if username:
                    password = get_secure_password()
                    create_account(username, password)

            elif account_choice == "L":
                if login():
                    # Start the simulation logic here
                    break

            else:
                print("Please choose only from [L] or [S]")

        except Exception as e:
            print("Invalid input:", e)


if __name__ == "__main__":
    main()
    # Dev notes: XAV WAS HERE AND THIS IS FUCKING SICKKKKKKKKKKKK

