# Created By: Pranav Sure
# Created Date: 5/10/2024
# version = '1.0'
# -----------------------------------------------------
"""This file is a basic way for the user(and ride operator) to interact and pick where they will be going"""
# -----------------------------------------------------
# Built in Imports
import time
from datetime import datetime
import os
import sys
from random import *
# -----------------------------------------------------
# User Made Imports and 3rd party imports
import rides
import concessions
import general
import roperator
from rich.progress import track
# -----------------------------------------------------

#this is meant to be used in IDLE


## password code

#stored password
customer_password = "123"
ride_operator_password = "r123"
#ask for password

password_inputted = input("Input '123' to explore the park, or input 'r123' to check on the status of the rides")

#progress bar as wait
for step in track(range(0, 100, 5), "Checking Password..."):
    time.sleep(randint(1, 200)/1000)

#password check loop
while True:
    #if user inputted customer password -> greet him
    if password_inputted == customer_password:
        print("Welcome to Sriketh's Park, where fun doesn't exist.")
        break

    #else, if user password inputted a ride operator password, navigate to the ride operator page(by calling the roperator function)
    elif password_inputted == ride_operator_password:
        roperator.main()

    #tell user that the password is wrong
    else:
        print("Entered the wrong password, make sure you are entering the password correctly.")


## actual main code
while True:
    try:
        #a tuple containing all the pages we can navigate to(and quit, to quit the program)
        pages = (rides.main, concessions.main, general.main, quit)

        #tell user the date and time right now=
        print(datetime.now().strftime("Current Date and Time: %B %-d, %Y %I:%M:%S %p"))
        
        #tell the options, and ask user for their input
        navigation = int(input("Here are the options: 1.Go to Rides\n2. Go to Concessions\n3. Go to Park Rules and Timings\n4. Exit"))

        #if the number the user provides is not a good number(this another way of error handling)
        if navigation > len(pages):
            raise ValueError
        
        #navigate to that page by using the index given[calculated by subtracting 1 from the number given](or exit)
        pages[navigation - 1]()
    except ValueError:
        print("Value is invalid, try again")
