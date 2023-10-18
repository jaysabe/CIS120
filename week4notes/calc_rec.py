from main import input_int_in_range, input_string

from Rectangle import Rectangle

# or
'''
import main as cs
name = cs.input_string("What is your name")
'''

def get_dimensions():
    width = input_int_in_range("What is the width of the rectangle? ", 0, sys.maxsize)
    height = input_int_in_range("What is the height of the rectangle? ", 0, sys.maxsize)
    return width, height # this is a tuple


def calc_rec():
    width, height = get_diminsions()
    area = calc_rec_area(width, height)
    display_results(width, height, area)


def calc_rec_area(width, height):
    return width * height


# if you need a specific class:
print("Welcome to calculating a rectangle")
print(Rectangle)
# r = Rectangle.Rectangle()
r = Rectangle()
r.calc_rec()

