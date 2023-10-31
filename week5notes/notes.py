# notes


def main():
    # list of planets:
    planets = ["Mercury", "Venus", "Earth", "Mars",
               "Jupiter", "Saturn", "Uranus", "Neptune",
               "Pluto"]

    # for planet in planets:
    #     print(planet)

# debug statement: "name" in lists
    print()
    pos = 0
    while pos < len(planets):
        print(planets[pos])
        pos += 1

    # changing the list:
    planets[2] = "Terra"
    print ('~~~~~~~~~~~~~~~~')
    for planet in planets:
        print(planet)
    accessing(planets)
    # # Incorrect syntax:
    # # for planet in planets:
    # #     planet = planet.reverse()
    #
    # # Reversing list:
    # pos = 0
    # while pos < len(planets):
    #     planets[pos] = planets[pos][::-1]
    # # tuple syntax = '(<stuff>,<more stuff>)' -- can't change
    # remove method:
    planets.remove("Pluto")
    del planets[1]
    # same as .remove() -> del planets[planets.index("Mars")]


def accessing(planets):
    # accessing positions
    print(planets[2]) # prints
    print(planets[1:5]) # slice operator - returns a list
    print(planets[0:4:2]) # pos 0 to 4 , skips every 2
    print(planets[0:4:-1]) # empty list
    print(planets[4:0:-1]) # all but that the last ele
    print(planets[4::-1]) # all reversed
    print(planets[::]) # prints original list
    print(planets[::-1]) # prints org reversed

    planets.append("")
    planets.append("X")
    planets.insert(3, "Mars 2")
    for planet in planets[::-1]:
        print(planet)


if __name__ == "__main__":
    main()
