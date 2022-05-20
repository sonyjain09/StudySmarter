#from matplotlib.pyplot import get
from pip._vendor import requests
#from getUserInformation import *

#rushika
#return a route for how to get there

def get_directions(name_of_origin, name_of_destination)->list:
    """Given the name of an origin and the name of a destination return directions to get from the origin 
    to the destination"""
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + name_of_origin + "&destination=" + name_of_destination + "&key="

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    dir = response.json()["routes"][0]["legs"][0]["steps"]

    steps =[]

    for step in dir:
        steps.append(step["html_instructions"])
    
    return steps

def getDrivingTime(name_of_origin, name_of_destination)->str:
    """Given  two locations returns the time it takes to drive between them."""
    url = "https://maps.googleapis.com/maps/api/directions/json?origin=" + name_of_origin + "&destination=" + name_of_destination + "&key="

    payload = {}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)
    duration = response.json()["routes"][0]["legs"][0]["duration"]["text"]

    return duration

