# 1)
# Create a function called "car_at_light"
# It should take one parameter: "light"
# which gives the color of a traffic light.
# If the color is "red", the function should return
# "stop". If the color is "green", the function
# should return "go". If the color is "yellow"
# the function should return "wait". If the color
# is anything else, the function should raise
# an exception with the following message: 
# "Undefined instruction for color: <light>" 
# where <light> is the value of the parameter light.
#
def car_at_light(light):
    light = light.lower()
    if light == 'red':
        return 'stop'
    elif light == 'green':
        return 'go'
    elif light == 'yellow':
        return 'wait'
    else:
        raise Exception (f'Undefined instruction for color: {light}')

    

# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

def safe_subtract(value1: int,value2: int):
    try: 
        x = value1 - value2
        return x
    except TypeError: 
        print('None')
    
    
# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

a = {'name': 'John', 'last_name': 'Doe', 'birth': 1990}
b = {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}


def retrieve_age_eafp(input_dict):
    try:
        age_v = 2021 - input_dict['birth']
        input_dict.update({'age': age_v})
        print("{name} {last_name} is {age} years old".format(**input_dict))
    except KeyError:
        print('The dictionary does not have enough information to print the age')
    
    
def retrieve_age_lbyl(input_dict):
    if 'name' in input_dict and 'last_name' in input_dict and 'birth' in input_dict:
        age_v = 2021 - input_dict['birth']
        input_dict.update({'age': age_v})
        print("{name} {last_name} is {age} years old".format(**input_dict))
    else:
        print('The dictionary does not have enough information to print the age')
        

# 4)
# Imagine you have a file named data.csv. 
# Create a function called "read_data" that reads the file
# making sure to use to handle the fact 
# that it might not exist. 
#
def read_data(data):
    try:
        f = open(data)
    except IOError as e:
        print("File can't be accessed")
    else:
        with f:
            print(f.read())
            


# 5) Squash some bugs! 
# Find the possible logical errors (bugs) 
# in the code blocks below. Comment in each of them
# which logical errors did you find and correct them
### (a)

total_double_sum = 0
for elem in [10, 5, 2]:
    double = elem * 2
    total_double_sum += double # It was adding elem instead of double. Fixed!
    

### (b)
strings = ''
for string in ['I', 'am', 'Groot']:
    strings += string + " " # It was replacing the last value and concatenating twice the same element


### (c) Careful!
j=10
while j > 0:
   j -= 1 # It was counting to infinite, fixed to do count down from 10
   print(j)

### (d)
productory = 1 # The initial value should be 1, with 0 always returns 0, a * 0 = 0
for elem in [1, 5, 25]:
    productory *= elem


################################################
##### Try to use map and reduce in the next 3 exercises
# 6)
# Create a function called "count_simba" that counts
# the number of times that Simba appears in a list of
# strings. Example: 
# ["Simba and Nala are lions.", "I laugh in the face of danger.",
#  "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 
#

from functools import reduce

ex = ["Simba and Nala are lions.", "I laugh in the face of danger.",
 "Hakuna matata", "Timon, Pumba and Simba are friends, but Simba could eat the other two."] 

def count_simba(string):
    return string.count('Simba') 
    
reduce(lambda x,y: x+y, map(count_simba, ex))

# 7)
# Create a function called "get_day_month_year" that takes 
# a list of datetimes.date and returns a pandas dataframe
# with 3 columns (day, month, year) in which each of the rows
# is an element of the input list and has as value its 
# day, month, and year.
# 

# 8) 
# Create a function called "compute_distance" that takes
# a list of tuple pairs with latitude and longitude coordinates and 
# returns a list with the distance between the two pairs
# example input: [((41.23,23.5), (41.5, 23.4)), ((52.38, 20.1),(52.3, 17.8))]
# HINT: You can use geopy.distance in order to compute the distance
#

#################################################
# 9)
# Consider a list that each element can be an integer or
# a list that contains integers or more lists with integers
# example: [[2], 4, 5, [1, [2], [3, 5, [7,8]], 10], 1]. 
# create a recursive function called "sum_general_int_list"
# that takes as input this type of list 
# and returns the sum of all the integers within the lists
# for instance for list_1=[[2], 3, [[1,2],5]] 
# the result should be 13 
#
