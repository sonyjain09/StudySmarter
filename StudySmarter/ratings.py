import io
def add_rating(place, rating):
    """given the name of a place and a rating adds a rating to the rating.txt file for the place"""
    with open('rating.txt', 'r') as file:
        data = file.readlines()
    for i in range(len(data)):
        if place in data[i]:
            data[i] = data[i] + rating
    with open('rating.txt', 'w') as file:
        file.writelines(data)

def get_average_rating(place)->float:
    """given the name of a place returns the average rating from the rating.txt file"""
    with open('rating.txt', 'r') as file:
        data = file.readlines()
    for i in range(len(data)):
        if place in data[i]:
            rating_string = data[i+1]
            break
    sum = 0
    count = 0
    for i in range(len(rating_string)):
        if rating_string[i:i+1].isdigit():
            sum += int(rating_string[i:i+1])
            count += 1
    return sum/count



