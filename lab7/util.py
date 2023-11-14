def input_positive_val(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            print("Input must be a positive number. Please try again. ")
        except ValueError:
            print('Error. Not a valid input.')


def chk_char(prompt):
    while True:
        try:
            ch = str(prompt).upper()
            if ch == 'M' or ch == 'F':
                return ch
            print("Invalid input. Our DB currently only has gender counts "
                  "for males ('M') or females ('F'). Please try again. ")
            prompt = input("Enter 'M' for Male or 'F' for Female: ")
        except ValueError:
            print("Something went wrong. Please try again later. ")
            exit()


def validate_str(prompt):
    while True:
        try:
            is_string = str(prompt)
            if is_string.strip() == '':
                print('Not a valid entry. Please try again. ')
            else:
                return is_string
        except ValueError:
            print("Invalid entry. Please try again. ")


def validate_range(prompt, min_, max_):
    while True:
        try:
            value = int(prompt)
            print(value)
            print(min_, max_)
            if min_ <= value <= max_:
                return value
            print(f"Selected year must be between {min_} and {max_}. ")
            prompt = input("Enter a valid year (between 1915-2014): ")
        except ValueError:
            print("Invalid input! Please try again. ")
            prompt = input("Enter a valid year (between 1915-2014): ")



