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
            ch = str(input(prompt))
            ch = ch.toUpper()
            if ch == 'M' or ch == 'F':
                return ch
            print("Invalid input. Our DB currently only has gender counts "
                  "for males ('M') or females ('F'). Please try again. ")
        except ValueError:
            print("Something went wrong. Please try again later. ")
            exit()


def validate_str(prompt):
    while True:
        try:
            is_string = str(prompt)
            if is_string.strip() == '':
                print('Not a valid entry. Please try again. ')

        except ValueError:
            print("Invalid entry. Please try again. ")
        return is_string


def validate_range(prompt, min_, max_):
    while True:
        try:
            value = int(input(prompt))
            if min_ < value < max_:
                return value
            print(f"Selected year must be between {min_} and {max_}. Thank you. ")

        except ValueError:
            print("Invalid input! Please try again. ")

