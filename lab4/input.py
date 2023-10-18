# input file
# input file
# Fidel
CURR_BALANCE = 1000

def check_int_value(prompt):
  while True:
    try:
        value = int(input(prompt))
        if value < 0 or value > 5:
            print("Please enter valid entry")
        else:
            break
    except ValueError:
        print("Please int value")
  return value


def check_float_value(prompt):
  while True:
      try:
          value = float(input(prompt))
          if value < 0 or value > 10000000000:
              print("Please enter valid value")
          else:
              break
      except ValueError:
          print("Please enter valid value.")
  return value

# def input_in_range(prompt, min_, max_):
#     while True:
#         try:
#             value = input_int(prompt)
#             if min_ <= value <= max_:
#                 return value
#             print(f'Number must be between {min_} and {max_}.')
#
#         except ValueError:
#             print('Not an option! Please select either (1), (2) , or (3).')
#
#
# def input_int(prompt):
#     while True:
#         try:
#             value = int(input(prompt))
#             return value
#         except ValueError:
#             print('Error. Not a valid input.')