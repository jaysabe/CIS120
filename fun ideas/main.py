# idea - > reads in a file and converts all text to ASCII

with open('txt file', 'r') as file:
    lines = file.readlines()

    # iterate through each line
    for line in lines:
        for char in line:
            ascii_value = ord(char)

            # Convert to binary
            binary_rep = bin(ascii_value)

            print(binary_rep)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    open()
