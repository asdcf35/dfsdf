# Created By: Pranav Sure
# Created Date: 5/10/2024
# version = '1.0'
# -----------------------------------------------------
"""This file is a basic way for the user to interact and pick which ride they will be picking"""
# -----------------------------------------------------
# Built in Imports
import os
import time
from random import randint
# -----------------------------------------------------
# User Made Imports and 3rd Party Imports
import backend
from rich.console import Console
from rich.progress import *
# -----------------------------------------------------

def main():
    """This is the concession's stand, where there will be many different types of restaurant"""
   

    #main code
    while True:
        # clear terminal
        os.system('cls')
        #create new Console item(a thing I use to format the display how i want it to look like)
        console = Console()

        # the restaurants' menus(filenames)
        restaurant_files = ("Burger City.csv", "Bread Bitez.csv",
                            "Biryani Garden.csv")

        # the new locations 
        locations = ('Beside 1984','Next to Scenic River Cruise','Near the Entrance')
        #the restaurant objects
        restaurants = {}

        #convert restaurant menus to restaurant objects
        for restaurant_file in restaurant_files:
            #remove the .csv from the filenames, and use it as the key(the name of the restaurant) to make a restaurant object
            restaurants[restaurant_file[:-4]] = backend.Restaurant(
                restaurant_file[:-4], True, restaurant_file)
            
        
        #print all restaurants and locations(locations is at the same index as restaurant)
        print("Here is all the restaurants we have:")
        for index, restaurant in enumerate(restaurants.keys(), 1):
            print(f"{index}. {restaurant} - {locations[index-1]}")
        
        #ask user for restaurant selection or q
        number = input(
            "Enter one of the restaurants(number only), or q to quit")
        
        try:
            #one liner basically saying keep q if number is q, otherwise try to change as 
            number = "q" if number == "q" else int(number) - 1
            if number == "q":
                break
        
            #raise an error if the number is greater than the highest index in the restaurants dictionary
            if int(number) - 1 > len(restaurants) - 1:
                raise ValueError
            
            #get the name of the restaurant using the number as the index
            restaurant_selected = list(restaurants.keys())[number]
        #if the number is not inputted correctly, or if the number is too big value is invalid
        except ValueError:
            print("The value is invalid, please try again.")
        else:
            #using the display foods from the restaurant object
            restaurants[restaurant_selected].display_foods(console)
            #ask the user to go back to the restraunts
            console.print("\n\nEnter q to go back to the restaurants",
                          justify="center", style='green')
            #press q -> back to the restaurants
            backend.quit_no_input()
    


    #after, check if they want to see if the code fully runs
    check_for_run = input(
        "Do you want to check if the code fully runs?('y' for yes, anything else for no)"
    )
    #if yes('y'), continue onto the actual code
    if check_for_run == "y":
        print("Ok")
    #else(anything else) -> print goodbye and exit code
    else:
        print("Goodbye!")
        quit()
