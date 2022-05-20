#for each study spot use get information (hours, facilties, proximity) and our own csv information to return info ab spots
from calendar import week
from webbrowser import get
from numpy import number
from pip._vendor import requests
from getPlaces import *
#url = "https://maps.googleapis.com/maps/api/place/details/json?place_id=ChIJXQMDUA_XDIgRCMznJSyf--c&fields=name%2Crating%2Copening_hours&key=AIzaSyDwW9XrO8GQEbtHuN_6Nrc56nfHNc1tdSg"

payload={}
headers = {}

#returns place id of place
def get_place_id(place_name)->str:
    """given the name of a place returns the place_id that google would want"""
    #reading from csv file
    placeDirectory = readCSV("StudySpot.csv")
    all_places = placeDirectory["Name of Study Spot"].tolist()
    all_ids = placeDirectory["Place_ID"].tolist()

    #finding place_id of place_name
    place_id = ""
    for x in range(len(all_places)):
        if place_name == all_places[x]:
            place_id = all_ids[x]
            break
    return place_id

#returns hours of operation of place and whether it is currently open 
def get_hours(place_name)->str:
    """given the name of a place returns the hours that the place is open"""
    #getting place id
    place_id = get_place_id(place_name)
    
    #retrieving place information from API
    url_start = "https://maps.googleapis.com/maps/api/place/details/json?place_id="
    url_end = "&fields=name%2Copening_hours&key="
    url = url_start+place_id+url_end
    response = requests.request("GET", url, headers=headers, data=payload)
    place_info = response.text

    if place_info.find("open_now") == -1:
        return "Hours of " + place_name + " not available."
    #open_now
    open_now_idx = place_info.index("open_now")
    open_now_idx2 = place_info.find(',',open_now_idx+12,open_now_idx+20)
    open_now = place_info[open_now_idx+12:open_now_idx2]
    
    #full hours of operation
    open_hours_idx = place_info.index("weekday_text")
    sunday_idx = place_info.index("Sunday")
    open_hours_idx2 = place_info.find('\"',sunday_idx,sunday_idx+30)
    open_hours = place_info[open_hours_idx+30:open_hours_idx2+1]

    week_hours = open_hours.split(",")
    
    hours_formatted = []
    for x in range(len(week_hours)):
        hours_formatted.append(week_hours[x].strip())

    hours_res = ""
    for x in range(len(hours_formatted)):
        day = hours_formatted[x]
        hours_res += day[1:len(day)-1]
        if day.find("Sunday") == -1:
            hours_res += "\n"

    #return statement
    ret = ""
    if open_now == "true":
        ret += "Open Now!"
    else:
        ret += "Closed."
    
    ret+= "\n\n(Hours)\n"
    ret+=hours_res

    return ret

#returns contact information for place
def get_contact_info(place_name)->str:
    """given the name of a place returns the contact info of the place"""
    #getting place id
    place_id = get_place_id(place_name)
    
    #retrieving place information from API
    url_start = "https://maps.googleapis.com/maps/api/place/details/json?place_id="
    url_end = "&fields=name%2Cformatted_phone_number&key="
    url = url_start+place_id+url_end
    response = requests.request("GET", url, headers=headers, data=payload)
    place_info = response.text

    #getting phone number
    if place_info.find("formatted_phone_number") == -1:
        return "Contact information for " + place_name + " not available."
    number_idx = place_info.index("-")
    number_idx2 = place_info.find('\"',number_idx,number_idx+6)
    phone_number = place_info[place_info.index("("):number_idx2]

    return "Phone: " + phone_number

def get_rating(place_name)->str:
    """given the name of a place returns the rating of the place that google has stored"""
    #getting place id
    place_id = get_place_id(place_name)

    #retrieving place information from API
    url_start = "https://maps.googleapis.com/maps/api/place/details/json?place_id="
    url_end = "&fields=name%2Crating&key="
    url = url_start+place_id+url_end
    response = requests.request("GET", url, headers=headers, data=payload)
    place_info = response.text

    #getting rating
    if place_info.find("rating") == -1:
        return "Rating for " + place_name + " not available."
    rating_idx = place_info.index("rating")
    rating = place_info[rating_idx+10:rating_idx+13]

    return "Rating: " + rating