# Created By: Pranav Sure
# Created Date: 5/10/2024
# version = '1.0'
# -----------------------------------------------------
"""This file is a basic way for the user(and ride operator) to interact and pick where they will be going"""
# -----------------------------------------------------
# Built in Imports
from math import *
import os
import msvcrt # this is a thing that will only work for windows
# -----------------------------------------------------
os.system('py -m pip install pandas rich') #needed for the 3rd party imports
# User Made Imports and 3rd party imports
import pandas as pd
# -----------------------------------------------------


def quit_no_input():
    """A function that quits the program when user hits q(but doesn't use the input function)"""
    while True:
        #check if key has been pressed
        if msvcrt.kbhit():
            #find out what key it is and store it to key
            key = msvcrt.getch().decode('ASCII')
            #if the key is q, then break
            if key == "q":
                break

# rides
class Ride:
    """This is a Ride Object, it has different functions related to checking the age"""

    def __init__(self, name, age_range, desc, working) -> None:
        """Initializes the object. Gives it a name, age range, description, and if it is working or not"""
        self.name = name
        self.age_range = age_range
        self.desc = desc
        self.working = working

    def check_age(self, age) -> bool:
        """Check if it is in the range"""
        return self.age_range[0] < age and age < self.age_range[1]


def rides_from_file(filename="rides.csv", admin=False) -> dict[str, Ride]:
    """
    Making Ride objects from a file

    Parameters
    ---
    filename : str, path object or file-like object
        the filename or object that you wish to use(must work with read_csv)
    """
    # creates a Pandas Dataframe from a filename
    dataframex = pd.read_csv(filename)
    #locate all the rows where Working is equal to true(working in t)
    dataframex = dataframex.loc[dataframex["Working"] == True]
    dataframex.loc[:, "Max"] = dataframex.loc[:, "Max"].fillna(999999999)
    dataframex.loc[:, "Min"] = dataframex.loc[:, "Min"].fillna(0)
    dataframe = dataframex.to_dict("records")
    rides = {}
    for dictionary in dataframe:
        rides[dictionary["Name"]] = Ride(
            dictionary["Name"],
            (dictionary["Min"], dictionary["Max"]),
            dictionary["Description"],
            dictionary["Working"],
        )
    if admin == False:
        return rides
    else:
        return rides, dataframex


class Food_Item:
    def __init__(self, name, cost, available) -> None:
        self.name = name
        self.cost = cost
        self.available = available


class Restaurant:

    def __init__(self, name, open, filename) -> None:
        self.name = name
        self.open = open
        self.dataframe = pd.read_csv(filename)
        self.item_names = tuple(self.dataframe.loc[:, "Items"])
        self.items = [
            Food_Item(
                self.item_names[i],
                self.dataframe.loc[i, "Price"],
                self.dataframe.loc[i, "Available"],
            )
            for i in range(len(self.item_names))
        ]

    def display_foods(self, console, discount=0) -> None:
        os.system("cls")
        console.print(f"Welcome to {self.name}\n\n", justify="center")
        console.print(f"Menu", justify="center")
        console.print(f'{"":-^30}', justify="center")
        print_half = self.dataframe.get(["Items", "Price"])
        console.print(print_half.to_string(index=False), justify="center")
