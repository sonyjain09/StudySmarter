Introduction:
The Study Smarter App makes a user's life easier by considering their needs and giving them options for places to study based on these needs. Not only does it give users options for where they can study on campus based on factors such as facilities and proximity of the study spot, but it also provides additional information on these locations like ratings, hours and contact information and gives them directions for how to get there.

Technical Architecture:

choose_start()

The choose_start() method gets input from the user for where their starting location is and returns a string of the user's starting location. The methods list_of_places(), get_directions() and get_time() use the string returned by this method in their functionality. Python was used to write this method. Diya wrote this method.

choose_distance()

The choose_distance() method gets input from the user for how far they are willing to travel from their current location and returns a float of the user's distance they’re willing to travel. The method list_of_places() uses the float returned by this method in its functionality. Python was used to write this method. Diya wrote this method.

choose_facilities()

The choose_facilities() method gets input from the user for what facilities they want at their desired study spot and returns a list of these facilities. The method places_with_facilities() uses the list returned by this method in its functionality. Python was used to write this method. Diya wrote this method.

list_of_places()

The list_of_places() method uses the float returned from get_distance() and the string returned from choose_start() to go through the CSV file and return a list of places that are within the radius of what the user wants. The method places_with_facilities() uses the list returned by this method in its functionality. Python, pandas, and google maps API were used to write this method. Sony wrote this method.

places_with_facilities()

The places_with_facilities() method uses the list returned from choose_facilities() and the list returned from list_of_places() to go through the CSV file and reorders the list of places based on which one has the most desired facilities. The method choose_location() uses the list returned by this method in its functionality. Python and pandas were used to write this method. Khushi wrote this method.

choose_location()

The choose_location() method uses the list returned from places_with_facilities() and displays it for the user and asks them to choose one of the places. It then returns a string of the location the user chose. The methods get_directions(), get_time(), get_user_rating(), add_rating(), get_hours(), get_contact_info(), get_average_rating() and get_rating() use the string returned by this method in their functionality. Python was used to write this method. Diya wrote this method.

get_average_rating()

The get_average_rating() method uses the string returned by choose_location() and goes into the rating.txt file and calculates the average rating of the chosen place. It returns a float of the average rating that is displayed to the user. Python was used to write this method. Sony wrote this method.

get_rating()

The get_rating() method uses the string returned from choose_location() and gets the google rating for the place. It then returns a string of the rating which is displayed to the user. Python and the google maps API were used to write this method. Khushi wrote this method.

get_contact_info()

The get_contact_info() method uses the string returned from choose_location() and gets the contact info for the place. It then returns a string of the contact info which is displayed to the user. Python and the google maps API were used to write this method. Khushi wrote this method.

get_hours()

The get_hours() method uses the string returned from choose_location() and gets the hours the place is open. It then returns a string of the hours which is displayed to the user. Python and the google maps API were used to write this method. Khushi wrote this method.

get_approval()

The get_approval() method asks the user if they want to confirm their study spot and returns the user's input as a string. The program will not continue running until the user confirms the study spot. If they don’t confirm it they will be asked to pick a new study spot and the details of their new place will be displayed. Python was used to write this method. Sony and Khushi wrote this method.

get_directions()

The get_directions() method uses the string returned from choose_location() and the string returned from choose_start() and returns a string of the directions for how to get from one place to the other. This is displayed for the user. Python and the google maps API were used to write this method. Rushika wrote this method.

get_time()

The get_time() method uses the string returned from choose_location() and the string returned from choose_start() and a string for the method of transportation returns a string of how long it will take to get from one place to the other given the method of transportation. This is displayed for the user. Python and the google maps API were used to write this method. Sony, Khushi, and Rushika wrote this method.

get_user_rating()

The get_user_rating() method gets input from the user for what they rate their study spot. The method add_rating() uses the string returned by this method in their functionality. Python was used to write this method. Diya wrote this method.

add_rating()

The add_rating_function() uses the string returned by the get_user_rating() function and writes it to the rating.txt file to store it in the data. The method get_average_rating() uses the data that is written to the file by this method. Sony wrote this method.

Installation Instructions:
1)Install homebrew if needed
https://brew.sh/
2) Navigate to your terminal and run "brew install git"
3) Navigate to your terminal and run "brew install python3"
3) Click on the green "Code" button and copy the link
4) Go to your text editor and clone the repository using the link you copied above (if you don't have a text editor we recommend downloading visual studio code)
https://code.visualstudio.com/download
5) Navigate to your terminal and run "pip3 install pandas" 
6) Go to the "StudySmarter.py" file and run the file
7) Follow the instructions that show up on the console

Group Members and Roles:
Diya Aggarwal - Working with user interaction and handling faulty user input
Sonam Jain - Working with pandas, ratings and Google Maps API functionality involving places
Khushi Gupta - Working with pandas, user interface design and Google Maps API functionality involving place details
Rushika Kumarswamy - Working with Google Maps API functinality involving directions