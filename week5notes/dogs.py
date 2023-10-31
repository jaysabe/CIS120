# dogs

def init_dogs():
    return [
        "Corgi",
        "Lab",
        "German Shepard",
        "Yorkie",
        "Dachshaud"
    ]


def print_menu():
    print("""
    Welcome to the Dog List Manager!
    Please select an item from the menu below:
    
    p) Print list of dog breeds
    a) Add a dog to the list
    r) Remove an item from list
    x) Exit the program.
    """)


def get_choice():
    choices = ['x', 'p', 'a', 'r']
    while True:
        choice = input("What is your choice? ")
        if choice in choices:
            return choice.lower()
        print("Choice must be one of: ")
        for choice in choices:
            print(" ", choice)


def print_list(dogs):
    print("Known Dogs:")
    for dog in dogs:
        print(" ", dog)
    print()


def add_to_list(dogs):
    breed = input_string("What is the name of the breed? ")
    dogs.append(breed)

def remove_from_list(dogs):
    breed = input_string("Which breed do you want to remove? ")
    if breed in dogs:
        dogs.remove(breed)
    else
        print(f"{breed} is not on the list of breeds, but okay.")

def main():
    dogs = init_dogs()
    while True:
        print_menu()
        choice = get_choice()
        if choice == 'x':
            break
        elif choice == 'p':
            print_list()
        elif choice == 'a':
            add_to_list(dogs)
        elif choice == 'r':
            remove_from_list(dogs)


if __name__ == '__main__':
    main()