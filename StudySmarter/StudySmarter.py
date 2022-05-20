from getPlaces import *
from getUserInformation import *
from directions import *
from ratings import *
from placesDetails import *
#returns place id of user location
user_location = choose_start()


#ask user what facilities and radius they're looking for
#returns facilities as a list and radius as an int
wanted_facilities = choose_facilities()
radius = choose_distance()


#use places nearby to find list of places. go through the list and see which ones match in our csv file
#returns a list of places
place_list = list_of_places(user_location, radius)


#go through facilities and see matches for what user wanted 
#returns the list the user will want
user_list = places_with_facilities(wanted_facilities, place_list)


#let user pick a spot 
#returns the spot the user picked as a string
spot_picked = choose_location(user_list)


#print study spot details & ask for user confirmation
print("\n" + get_hours(spot_picked))
print("\n" + get_contact_info(spot_picked))
print("\n" + get_rating(spot_picked) + "\n")
confirmation = get_approval()
while confirmation == "N":
    spot_picked = choose_location(user_list)
    print("\n" + get_hours(spot_picked))
    print("\n" + get_contact_info(spot_picked))
    print("\n" + get_rating(spot_picked) + "\n")
    confirmation = get_approval()


#print a route for how to get there 
#returns directions as a string 
user_location = user_location + " Champaign Urbana Illinois University"
directions = get_directions(user_location,spot_picked)
print("\n")
pretty_direction = ""
for direction in directions:
    x = direction.replace("<b>", " ")
    y = x.replace("</b>", " ")
    z = y.replace("<div style=\"font-size:0.9em\">", " ")
    n = z.replace("</div>", " ")
    r = n.replace("/<wbr/>","")
    pretty_direction = pretty_direction + r + "\n"
print(pretty_direction)


#return the time it will take to get to the chosen study spot
print("\nDriving duration: " + get_time(user_location,spot_picked,"driving"))
print("\nWalking duration: " + get_time(user_location,spot_picked,"walking"))
print("\nBiking duration: " + get_time(user_location,spot_picked,"biking")+"\n")


#get user rating and add it to the file
rating = get_user_rating()
add_rating(spot_picked, rating)