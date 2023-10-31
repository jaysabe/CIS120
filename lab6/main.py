#******************************************************************************
# Author:           Jay Abegglen
# Lab:              6
# Date:             10/25/2023
# Description:      Program takes in information from the US Census and then prints
# them in terms of their name, birth year, gender, and count
# Input:            Input comes from Database class
# Output:           Displays attributes from Name class
# Sources:          Lab 6 specifications
#                   Note: Completed on own due to traveling this week.
#******************************************************************************

from Name import Name


def main():
    # Fetch data:
    names = Name.read_names()

    print("\n\tUS CENSUS\n")
    # Display information
    i = 1
    for name in names:
        print(f"{str(i)+ '.) '}Name: {name.get_name()}, Year: {name.get_year()}, "
              f"Gender: {name.get_gender()}, Count: {name.get_count()}")
        i += 1



# *********************************
if __name__ == "__main__":
    main()
