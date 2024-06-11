def print_student_info(data_structure):
    # Get the first name from full one
    first_name = data_structure["full_name"].split()[0]
    # Print student info
    print(f"My name is {data_structure['full_name']}, but you can call me Mr {first_name}.")
    print(f"My student ID is {data_structure['student_id']}.")

def main():

    # TWO: Create a Complex Data Structure
    my_info = {
        "full_name": "Nisharg Patel ",
        "student_id": 10324039,
        "pizza_toppings": ["SPINACH", "RELISH", "JALAPENOS"],
        "movies": [
            {"title": "Doctor do little", "genre": "comedy"},
            {"title": "Black Panther", "genre": "sci-fi"}
        ]
    }

    # THREE: Data structure with new movie 
    new_movie = {"title": "iron-man", "genre": "action"}
    my_info["movies"].append(new_movie)

    # FOUR: Printing student information 
    print_student_info(my_info)

    #Topping list before adding new toppings 
    print_pizza_toppings(my_info)

    # FIVE: Adding toppings 
    additional_toppings = ("PINEAPPLE", "CHICKEN")
    add_pizza_toppings(my_info, additional_toppings)

    # SIX: Bullet list of pizza toppings after editing 
    print_pizza_toppings(my_info)

    # SEVEN: Movie genres separated by commas 
    print_movie_genres(my_info)

    # EIGHT: Movie headings separated by commas 
    print_movie_titles(my_info["movies"])
def add_pizza_toppings(data_structure, toppings):
    # add pizza toppins to topping list 
    data_structure["pizza_toppings"].extend(toppings)
    # change toppings to lowercase
    data_structure["pizza_toppings"] = sorted([topping.lower() for topping in data_structure["pizza_toppings"]])

def print_pizza_toppings(data_structure):
    # Display sentence
    print("My favourite pizza toppings are:")
 
    for topping in data_structure["pizza_toppings"]:
        print(f"- {topping}")

def print_movie_genres(data_structure):
    genres = [movie["genre"] for movie in data_structure["movies"]]
    # Print the sentence with commas 
    print(f"I like to watch {', '.join(genres[:-1])}, and {genres[-1]} movies.")

def print_movie_titles(movie_list):
    titles = [movie["title"].title() for movie in movie_list]
    # Print the sentence with commas 
    print(f"Some of my favourite movies are {', '.join(titles[:-1])}, and {titles[-1]}!")

    # ONE: Starting with def main function and if statement

if __name__ == '__main__':
    main()