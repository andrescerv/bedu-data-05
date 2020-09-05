from helper_functions import double_number

numbers_list = [
    8,
    10,
    23,
    38,
    126,
    18,
    19,
    22,
    9
]

#--doubling a value---------------------------------------
def double_number(value):
    return value * 2

number = 2500
number_double = double_number(number)

#--doubling a list of values-------------------------------
for n in numbers_list:
    r = double_number(n)
    return r
