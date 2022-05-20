from getPlaces import*
from placesDetails import*
from ratings import *
#writing tests
#testing list_of_places
def testing_list_of_places():
    #test with .5 radius
    par_list_x = list_of_places("Pennsylvania Avenue Residence", .5)
    assert(set(par_list_x) == set(["Funk Agricultural, Consumer, and Environmental Sciences Library (Funk ACES)"]))
    print("testing_list_of_places(): .5 radius tests passed")

    #test with .75 radius
    here_list_x = list_of_places("HERE", .75)
    assert(set(here_list_x) == set(['Grainger Engineering Library', 'Campus Instructional Facility (CIF)', 'Business Instructional Facility', 'Electrical and Computer Engineering Building', 'Siebel Center for Design', 'Thomas M. Siebel Center for Computer Science', 'BrewLab Coffee', 'Undergraduate Library', 'Illini Union', 'Ikenberry Commons Residence Hall Library', 'Krannert Center for the Performing Arts', 'Sidney Lu Mechanical Engineering Building', 'Loomis Laboratory Of Physics, University Of Illinois', 'Communications Library', 'Etc. Coffeehouse', 'Beckman Institute', 'Everitt Laboratory']))
    print("testing_list_of_places(): .75 radius tests passed")

    #test with 1 radius
    isr_list_x = list_of_places("Illinois Street Residence", 1.0)
    assert(set(isr_list_x) == set(['Grainger Engineering Library', 'Campus Instructional Facility (CIF)', 'Business Instructional Facility', 'Funk Agricultural, Consumer, and Environmental Sciences Library (Funk ACES)', 'Electrical and Computer Engineering Building', 'Thomas M. Siebel Center for Computer Science', 'BrewLab Coffee', 'Caffe Bene', 'Undergraduate Library', 'Illini Union', 'Krannert Center for the Performing Arts', 'Sidney Lu Mechanical Engineering Building', 'Loomis Laboratory Of Physics, University Of Illinois', 'Music and Performing Arts Library', 'Communications Library', 'Etc. Coffeehouse', 'Beckman Institute', 'Everitt Laboratory']))
    print("testing_list_of_places(): 1.0 radius tests passed")

    #test with 1.5 radius
    weston_list_x = list_of_places("Weston Hall", 1.5)
    assert(set(weston_list_x) == set(['Grainger Engineering Library', 'Campus Instructional Facility (CIF)', 'Business Instructional Facility', 'Funk Agricultural, Consumer, and Environmental Sciences Library (Funk ACES)', 'Electrical and Computer Engineering Building', 'Siebel Center for Design', 'Thomas M. Siebel Center for Computer Science', 'BrewLab Coffee', 'Caffe Bene', 'Undergraduate Library', 'Illini Union', 'Ikenberry Commons Residence Hall Library', 'Krannert Center for the Performing Arts', 'Sidney Lu Mechanical Engineering Building', 'Loomis Laboratory Of Physics, University Of Illinois', 'Music and Performing Arts Library', 'Communications Library', 'Etc. Coffeehouse', 'Beckman Institute', 'Everitt Laboratory']))
    print("testing_list_of_places(): 1.5 radius tests passed")
    
#testing places_with_facilities
def testing_places_w_facilities():
    #simple test
    facilities_list = ["cafe/restaurant","vending machine"]
    places_list = ["Beckman Institute","Illini Union","Everitt Laboratory"]
    test = ["Illini Union","Beckman Institute","Everitt Laboratory"]
    func_result = places_with_facilities(facilities_list, places_list)
    assert(test == func_result)
    print("testing_places_w_facilities(): simple test passed")

    #test with same number of facility matches
    facilities_list2 = ["cafe/restaurant","vending machine"]
    places_list2 = ["Beckman Institute","Illini Union","Grainger Engineering Library"]
    test2 = ["Illini Union","Grainger Engineering Library","Beckman Institute"]
    func_result2 = places_with_facilities(facilities_list2, places_list2)
    assert(test2 == func_result2)
    print("testing_places_w_facilities(): test 2 passed")

    #test with no matches
    facilities_list3 = ["classrooms","printer"]
    places_list3 = ["BrewLab Coffee","Illini Union","Krannert Center for the Performing Arts"]
    test3 = ["BrewLab Coffee","Illini Union","Krannert Center for the Performing Arts"]
    func_result3 = places_with_facilities(facilities_list3, places_list3)
    assert(test3 == func_result3)
    print("testing_places_w_facilities(): test 3 passed")

def testing_places_details():
    #contact info tests
    siebel_num = "Phone: (217) 300-9100"
    funct_res = get_contact_info("Siebel Center for Design")
    assert(siebel_num == funct_res)
    print("testing get_contact_info(): test 1 passed")

    commun_num = "Phone: (217) 333-2216"
    funct_res = get_contact_info("Communications Library")
    assert(commun_num == funct_res)
    print("testing get_contact_info(): test 2 passed")

    everitt_num = "Phone: (217) 333-1867"
    funct_res = get_contact_info("Everitt Laboratory")
    assert(everitt_num == funct_res)
    print("testing get_contact_info(): test 3 passed")

    #rating tests
    caffe_bene_rat = "Rating: 4.4"
    funct_res = get_rating("Caffe Bene")
    assert(caffe_bene_rat == funct_res)
    print("testing get_rating(): test 1 passed")
    
    siebel_cs_rat = "Rating: 4.8"
    funct_res = get_rating("Thomas M. Siebel Center for Computer Science")
    assert(siebel_cs_rat == funct_res)
    print("testing get_rating(): test 2 passed")

    krannert_rat = "Rating: 4.8"
    funct_res = get_rating("Krannert Center for the Performing Arts")
    assert(krannert_rat == funct_res)
    print("testing get_rating(): test 3 passed")

def testing_ratings():
    add_rating("Beckman Institute", "4")
    with open('rating.txt', 'r') as file:
        data = file.readlines()
    for i in range(len(data)):
        if "Beckman Institute" in data[i]:
            rating_string = data[i+1]
            rating = rating_string[0]
    assert(rating == "4")
    print("testing add_rating() passed")
    
    avg = get_average_rating("Testing Place")
    assert(avg == 3.25)
    print("testing get_average_rating() passed")









#calling tests
testing_list_of_places()
testing_places_w_facilities()
testing_places_details()
testing_ratings()
print("all tests passed")
