# Created By: Pranav Sure
# Created Date: 5/10/2024
# version = '1.0'
# -----------------------------------------------------
"""This file is a basic way for the user to interact and pick which ride they will be picking"""
# -----------------------------------------------------
# Built in Imports
import os
from time import sleep
import msvcrt

# -----------------------------------------------------
# User Made Imports and 3rd Party Imports
from backend import *
from rich.console import Console
# -----------------------------------------------------
#creates a console class(this allows us to do more than what regular print does)
console = Console()
#creates another console class
ride_desc_console = Console()

def disp_ride(ride) -> None:
    """
    Displays the ride in a presentable way

    Parameters:
    ride : the current ride that is being used
    """
    #clear the system
    os.system("cls")
    #print the ride name
    print("Ride:", ride.name)
    ride_desc_console.print(f'{ride.desc}',justify='center')
    print("\n\n\n")
    console.print("Hit q to return back.",justify='center', style="green")
    quit_no_input()


def main():
    rides = rides_from_file("rides.csv")

    # create variable holding list of all rides
    list_of_rides = "Here is a list of all the rides:\n"
    # add all the rides (formatted: <<Index Number>>. <<Ride Name>>)
    for index, ride_name in enumerate(rides.keys()):
        list_of_rides += f"\t{index + 1:>2}. {ride_name}\n"

    # ask user(numbers)
    while True:
        try:
            # Print all the rides
            os.system('cls')
            print("Welcome to the Amusement Park!\n")
            sleep(1)
            print(list_of_rides)
            # ask the user which ride they want to go to
            user_ride = input(
                "Pick the ride you want to go on, or type q if you want to exit.(numbers only)\n"
            )
            # if the user enters q(exit value), exit
            if user_ride == "q":
                print(
                    "Thank you for visiting the Amusement Park!"
                )
                sleep(2)
                break
            else:
                # set user_ride to the name of the ride(stored in the specific index of the keys of the rides)
                user_ride = list(rides.keys())[int(user_ride) - 1]
                print(user_ride)

        except Exception as e:
            print("Input is invalid. Please try again.")
            print(e)
        else:
            # check if there is any age restrictions(if it is not 0 and obscenely high number) 
            if rides[user_ride].age_range == (0, 999999999):
                disp_ride(rides[user_ride])
            else:
                print(
                    f"The {user_ride} is a great choice! However we need to check your age."
                )
                age = int(input("What is your age? "))

                # TODO: use age_check function(returns true if in the correct value, else False
                if rides[user_ride].check_age(age):
                    disp_ride(rides[user_ride])
                else:
                    print("Sorry we can't let you go in.\n")
                    console.print("Hit q to return back.")
                    quit_no_input()