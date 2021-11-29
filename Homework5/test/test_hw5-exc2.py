# 2)
# Create a function named "safe_subtract" that
# takes two parameters and returns the result of
# the second value subtracted from the first.
# If the values cannot be subtracted due to its type, 
# it returns None.
# If there is any other reason why it fails show the problem 
# 

def test_safe_subtract_1():
    x1 = 5
    x2 = 3
    output = safe_subtract(x1, x2)
    expected_output = 2
    assert output == expected_output
    
    
def test_safe_subtract_2():
    x1 = 10
    x2 = 30
    output = safe_subtract(x1, x2)
    expected_output = -20
    assert output == expected_output


