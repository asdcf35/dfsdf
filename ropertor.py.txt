# Created By: Pranav Sure
# Created Date: 5/10/2024
# version = '1.0'
# -----------------------------------------------------
"""This file is a basic way for the user(ride operator) to have a way to interact and change the rides"""
# -----------------------------------------------------
# Built in Imports
from re import I
import time
import os
import sys
from random import randint
# -----------------------------------------------------
# User Made Imports and 3rd party imports
import rides
import concessions
import water_park
import backend
from time import sleep
from rich.progress import track
import pandas as pd
# ----------------------------------------------------



def main():
    os.system('cls')
    #print that ride operator is detected
    print("\n\nRide Operator Detected\n\n")

    #similar to a sleep function(but looks cooler imho)
    for step in track(range(0, 100, 10), "Loading the Console..."):
        time.sleep(randint(100, 200) / 1000)

    while True:
        """Interface that allows the ride operator to change the status of the rides, working or not working"""
        os.system("cls")  # system clear
        # rides
        rides, dataframe = backend.rides_from_file("rides.csv", admin=True)
        list_of_rides = "Here is all the rides:\n"
        # add all the rides (formatted: <<Index Number>>. <<Ride Name>>)
        for index, ride_name in enumerate(rides.keys()):
            list_of_rides += f"\t{index + 1:>2}. {ride_name}\n"

        #print the string
        print(list_of_rides)
        try:
            #as the user which ride they want to edit
            user_ride = int(
                input(
                    "Pick the ride you want to edit, or type q if you want to exit.(numbers only)\n"
                ))
            #if the input given is greater than the length of the rides, give a value error
            if user_ride> len(rides):
                raise ValueError
        except ValueError:
            print("Not a valid input, try again")
            sleep(2)
        else:
            # set user_ride to the name of the ride(stored in the specific index of the keys of the rides)
            row_to_edit = dataframe.loc[dataframe["Name"] == list(rides.keys())
                                        [user_ride - 1]].index[0]

            list_of_properties = tuple(dataframe.columns)
            #list all the options(should not change no matter what)
            print("Options to change: ")
            for index,property in enumerate(list_of_properties, 1):
                print(f"\t{index}.{property}")
            #ask user to edit the format(str, because it's easier)
            edit_format = input("What do you want to change(1 - 5): ")

            #ask the user for the final amount
            change = input("What are you changing it to: ")

            #if they want to edit the name, change the name
            if edit_format == '1':
                dataframe.loc[row_to_edit, 'Name'] = change

            #check if they want to edit the min age
            elif edit_format == '2':
                #check if the integer is an input
                try:
                    change = int(change)

                #if the value error is not a valid input
                except ValueError:
                    print("Sorry, not a valid input")

                #update the change
                else:
                    dataframe.loc[row_to_edit, 'Min'] = change

            #check if they want to edit the min age
            elif edit_format == '3':
                #check if the integer is an input
                try:
                    change = int(change)

                #if the value error is not a valid input
                except ValueError:
                    print("Sorry, not a valid input")

                #update the change
                else:
                    dataframe.loc[row_to_edit, 'Max'] = change

            #check if they want to edit the description
            elif edit_format == '4':
                dataframe.loc[row_to_edit, 'Description'] = change

            #check if the ride is working
            elif edit_format == '5':
                #check if the change is not in true or false
                if change.lower() not in ("true", "false"):
                    print("Sorry, not a valid input")

                #change it to true or false depending on the answer
                else:
                    change = False if change.lower() == "false" else True
                    dataframe.loc[row_to_edit, 'working'] = change
            else:
                print("Sorry not a valid input")
                continue
            #print the edited csv
            print("Here is that data:", dataframe, sep="\n")

            #print the rides
            dataframe.to_csv("rides.csv")
            break


if __name__ == "__main__":
    main()
