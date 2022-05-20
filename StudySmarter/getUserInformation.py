import pandas as pd
from pip._vendor import requests
import googlemaps
from ratings import *
from numpy import choose

#diya
#ask user what facilities and things they're looking for (give them options)

def choose_start()->str:
    """Gets user input for what the users starting location is"""
    loc = input("Please input your current location.\n")
    return loc


# def chooseSize()->str:
#     """Gets user input for what size facility the user wants"""
#     size = input("Please enter the size of the study spot you are looking for. Your choices are small, medium, or large.")
#     try:
#         assert(size == "small" or size == "medium" or size == "large") 
#     except:
#          print("Please type either small, medium, or large.")
#          chooseSize()
#          exit()
#     return size


def choose_facilities()->list:
    """Gets user input for what facilities the user wants"""
    facilities = []
    numFacilities = int(input("\nPlease enter the number of facilities you are looking for from these options: Cafe/Restaurant, Vending Machine, Printers, Loanable Technology, Wifi, Classrooms.\n"))
    try:
        assert(numFacilities>0) 
    except:
         print("\nPlease type a positive number of facilities\n")
         choose_facilities()
         exit()
    print("\nPlease enter the facility numbers you would like, line by line")
    print("\n1\tCafe/Restaurant\n\n2\tVending Machine\n\n3\tPrinters\n\n4\tLoanable Technology\n\n5\tWifi\n\n6\tClassrooms\n")
    for i in range(0, numFacilities):
        element = input()
        if element == 1:
            facilities.append("Cafe/Restaurant")
        if element == 2:
            facilities.append("Vending Machine")
        if element == 3:
            facilities.append("Printers")
        if element == 4:
            facilities.append("Loanable Technology")
        if element == 5:
            facilities.append("Wifi")
        if element == 6:
            facilities.append("Classrooms")
    
    return facilities

def choose_distance()->float:
    """Gets user input for how far the user is willing to travel"""
    distance = input("\nPlease enter the distance (in miles) you are willing to travel (0.25, 0.5, 0.75, 1.0, and 1.5)\n ")
    return float(distance)

def choose_location(list_of_locations)->str:
    """Given a list gets input for which location the user wants to travel to"""
    print("\nPlease enter the number of the location that you would like to study at in order to see directions.\n Location reviews have been provided as well.\n")
    count = 1
    for x in list_of_locations:
        print(count, " ", x)
        print("\tAverage User Rating: " + str(get_average_rating(x)) + "\n")
        count=count+1
    num = int(input())
    location = list_of_locations[num-1]
    return location

def get_user_rating()->str:
    """Gets the users rating for the study spot they chose"""
    rating = input("Please give your chosen study spot a rating out of 5.\n")
    return rating

def get_approval()->str:
    """Gets the users approval for their study spot"""
    answer = input("Confirm study spot (Y/N)\n")
    return answer