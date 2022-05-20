from ctypes import LibraryLoader
import pandas as pd
from pip._vendor import requests
from directions import *

#sony
#make dataframe with csv file
def readCSV(filename)->pd.DataFrame:
    """Given the name of a file return a data frame containing the information in the file"""
    df = pd.read_csv("StudySpot.csv")
    return df


def within_radius(location_one, location_two, radius)->bool:
    """Given two locations and a radius returns wether or not the distance between the two is less
    than or equal to the radius"""
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={location_one}&destinations={location_two}C&mode=walking&language=fr-FR&unit=miles&key='
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    dist = response.json()["rows"][0]["elements"][0]["distance"]["text"]
    dist = dist.replace(",", ".")
    if(dist[-2] == "k"):
        km = float(dist.replace(" km",""))
        miles = km / 1.609
    else:
        m = float(dist.replace(" m",""))
        miles = m * 0.000621371
    if miles <= radius:
        return True
    return False


def get_time(location_one, location_two, mode)->str:
    """given two locations and a mode returns how long it will take to travel between two places given a mode"""
    url = f'https://maps.googleapis.com/maps/api/distancematrix/json?origins={location_one}&destinations={location_two}C&mode={mode}&language=fr-FR&unit=miles&key='
    payload={}
    headers = {}
    response = requests.request("GET", url, headers=headers, data=payload)
    time = response.json()["rows"][0]["elements"][0]["duration"]["text"]
    return time


#sony
#use places nearby to find list of places. go through the list and see which ones match in our csv file
def list_of_places(location_name, radius)->list:
    """given the name of a location and a radius goes through the csv file and returns a list of 
    places that are within the radius"""
    location_name = location_name + " Champaign Urbana Illinois University"
    place_directory = readCSV("StudySpot.csv")
    places = place_directory["Name of Study Spot"].tolist()
    output = []
    #go through dataframe and match places with csv places
    #also make sure is within radius
    for match in places:
        if within_radius(match, location_name,radius):
            output.append(match)
    #return list of places that match
    return output

def extra_places(location_name, radius)->list:
    """Given the name of a location and a radius returns a list of places nearby the location using the 
    places nearby function of google maps api"""
    #get the longitude and latitude of place id with geocode
    payload={}
    headers = {}
    location_name = location_name + " Champaign Urbana Illinois University"
    url1 = f'https://maps.googleapis.com/maps/api/geocode/json?address={location_name}&key='
    response = requests.request("GET", url1, headers=headers, data=payload)
    lat = response.json()["results"][0]["geometry"]["location"]["lat"]
    lng = response.json()["results"][0]["geometry"]["location"]["lng"]
    #use latitude and longitude to get places nearby with nearbysearch 
    url2 = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&radius={radius}&rankyby=distance&type=library&keyword=study&key='
    url3 = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&radius={radius}&rankyby=distance&type=restaurant&keyword=study&key='
    url4 = f'https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat}%2C{lng}&radius={radius}&rankyby=distance&type=cafe&keyword=study&key='
    lib_responses = requests.request("GET", url2, headers=headers, data=payload)
    rest_responses = requests.request("GET", url3, headers=headers, data=payload)
    cafe_responses = requests.request("GET", url4, headers=headers, data=payload)
    #make a list of places nearby 
    lib_list = lib_responses.json()["results"]
    rest_list = rest_responses.json()["results"]
    cafe_list = cafe_responses.json()["results"]
    place_names = []
    for place in lib_list:
        place_names.append(place["name"])
    for place1 in rest_list:
        place_names.append(place1["name"])
    for place2 in cafe_list:
        place_names.append(place2["name"])
    #remove duplicates
    all = []
    for i in place_names:
        if i not in all:
            all.append(i)
    return all


#takes in listofplaces(radius) and returns list sorted by user chosen facilities
def places_with_facilities(facilities_list, places_list)->list:
    """Given a list of facilities and list of places returns a list of places in order for
    which one has the most wanted facilities"""
    #list of all places and facilities from file
    placeDirectory = readCSV("StudySpot.csv")
    all_places = placeDirectory["Name of Study Spot"].tolist()
    all_facilities = placeDirectory["Facilities"].tolist()

    #list of indexes corresponding to places_list from all_places
    place_indexes = []
    for x in range(len(places_list)):
        for y in range(len(all_places)):
            if places_list[x] == all_places[y]:
                place_indexes.append(y)
                break
    
    #list of facilities corresponding to places_list
    places_facilities = []
    for x in range(len(place_indexes)):
        places_facilities.append(all_facilities[place_indexes[x]])

    #list storing number of facilities corresponding to places_list
    num_facilities = []
    for facility in places_facilities:
        chosen_place_facilities = facility.split(",")
        count = 0
        for curr_place_fac in chosen_place_facilities:
            for curr_user_fac in facilities_list:
                if curr_place_fac == curr_user_fac:
                    count = count + 1
        num_facilities.append(count)

    #list with sorted places using num_facilities w corresponding number of matching facilities
    places_in_order = []
    while len(places_in_order) < len(places_list):
        max_num_facil = max(num_facilities)
        index = num_facilities.index(max_num_facil)
        places_in_order.append(places_list[index])
        num_facilities[index] = -1
        
    return places_in_order