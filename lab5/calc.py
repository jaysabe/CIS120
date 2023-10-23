# calculations page


def chk_price(inp):
    while True:
        try:
            if inp > 0:
                return inp
            else:
                print('Invalid input. Must be a positive price. please try again.')
        except ValueError:
            print('Invalid input. Must be a number. please try again.')


def check_cart(smoothies):
    if len(smoothies) == 0:
        print("There are no smoothies in your cart currently. \n")
        return
    else:
        i = 1
        for smoothie_name in smoothies:
            # row = smoothie_name
            print(str(i) + ".) " + smoothie_name)
            i += 1
            print()


def mod_smoothie(smoothies, typeof):
    new_name = input("Smoothie Name: ")
    if typeof == "add" and new_name in smoothies:
        print(new_name + " is already a smoothie in our list.")
        resp = input("Would you like to edit it? (y/n): ").lower()
        if resp != 'y':
            return
    elif typeof == "change" and new_name not in smoothies:
        print(new_name + " doesn't exist in your cart yet.")
        resp = input("Would you like to edit it? (y/n): ").lower()
        if resp != "y":
            return

    price = chk_price(float(input("Price: ")))
    fruit = input("Fruit (additional seperated with a \'-\'): ")
    base = input("Enter base: ")
    sweetener = input("Enter sweetener: ")

    # Add inputs to dictionary
    smoothie = {"price": price, "fruit": fruit, "base": base, "sweetener": sweetener}

    # add smoothie to cart
    smoothies[new_name] = smoothie

    # ternary results:
    results = "added to" if typeof == 'add' else "updated in" if typeof == 'change' else None
    print(f"Your smoothie has been {results} cart") \
        if (typeof == 'add' or typeof == 'change') \
        else print("Something went wrong, please try again")


def remove_smoothie(smoothies):
    name = input("Name: ")
    if name in smoothies:
        del smoothies[name]
        print(name + " was removed from the cart.")
    else:
        print(name + " does not exist in our menu.")


def cart_stats(smoothies):
    smoothie = input("Enter a smoothie: ")
    if smoothie in smoothies:
        name = smoothies[smoothie]
        print("Name: ", name)
        print("Price: ", str("${:,.2f}".format(name["price"])))
        print("Ingredients: " + name["fruit"] + "," + name["base"] + "," + name["sweetener"])
    else:
        print("Sorry, this " + smoothie + " smoothie is not in our cart.")


