# Notes week2
# python uses lower snake case / is more common then lowerCamel case -- pick one or the other
# UPPER_SNAKE case for const, capital case Classes

def testme(name):
    name = input("What is your name? ")
    if name == "":
        print('Err! Name cannot be empty.')
        exit(0)
    return name
# python uses 4 space indents

# Example -- minutes on a game mission


def get_missions():
    missions = round(float(input("How many missions have you completed? ")))
    return missions


def get_minutes():
    minutes = int(input("How long have you been playing for? "))
    return minutes


def calc_avg_minutes(missions, minutes):
    average_min = minutes / missions

    return average_min


def print_results(missions, minutes, average_min):
    print(f"You completed {missions} missions")
    print(f"You have spent {minutes}")
    print(f"You have spent an average of {average_min} minutes")


def main():
    name = testme()
    print("Welcome to my video game mission program, {}! \n", format(name))
    missions = get_missions()
    minutes = get_minutes()
    average_min = calc_avg_minutes(missions, minutes)
    print_results(missions, minutes, average_min)


if __name__ == '__main__':
    main()