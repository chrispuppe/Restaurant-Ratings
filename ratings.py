"""Restaurant rating lister."""

rating_list = []

with open('scores.txt') as f:
    for line in f:
        (resturant, rating) = line.split(':')
        dict = {'resturant': resturant.strip(), 'rating': int(rating.strip())}
        rating_list.append(dict)

def sort_print_my_dict_list():
    sorted_ratings =  sorted(rating_list, key=lambda x:x['resturant'])

    for i in sorted_ratings:
        rating = i['rating']
        resturant = i['resturant']
        print(f"{resturant} is rated at {rating}.")

def add_new_resturant():
    new_resturant = input("What is the resturant's name? ")
    new_resturant_rating = input("What is the resturant's rating? ")
    new_resturant_profile = {'resturant': new_resturant.strip(),
                            'rating': int(new_resturant_rating.strip())}

    rating_list.append(new_resturant_profile)
    sort_print_my_dict_list()

sort_print_my_dict_list()
add_new_resturant()
