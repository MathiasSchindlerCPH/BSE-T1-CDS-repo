# 1)
# Create a function named
# "triple" that takes one
# parameter, x, and returns
# the value of x multiplied
# by three.
#
def triple(a):
    y = 3*a
    return y



# 2)
# Create a function named "subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
#
def subtract(a,b):
    x = b - a
    return x


# 3)
# Create a function called "dictionary_maker"
# that has one parameter: a list of 2-tuples.
# It should return the same data in the form
# of a dictionary, where the first element
# of every tuple is the key and the second
# element is the value.
#
# For example, if given: [('foo', 1), ('bar', 3)]
# it should return {'foo': 1, 'bar': 3}

def dictionary_maker(a):
    for i in range(len(a)):
        if not isinstance(a[i], tuple) & (len(a[i]) == 2):
            raise TypeError
    else:
        dict = {a[0][0]: a[0][1]}
        for i in range(1, len(a)):
            dict2 = {a[i][0]: a[i][1]}
            dict.update(dict2)
    return dict




test1 = [("foo", 1), ("bar", 3), ("cop", 15), ("hello", 26), ("world", 45)]
test99 = [("bar",3,3), ("bar", 3), ("cop", 15), ("hello", 26), ("world", 45)]

dictionary_maker(test1)
dictionary_maker(test99)
