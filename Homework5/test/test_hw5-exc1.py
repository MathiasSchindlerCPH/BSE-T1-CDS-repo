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

def test_car_at_light_1():
    x = 'red'
    output = car_at_light(x)
    expected_output = 'stop'
    assert output == expected_output
    
def test_car_at_light_2():
    x = 'yellow'
    output = car_at_light(x)
    expected_output = 'wait'
    assert output == expected_output
    
def test_car_at_light_3():
    x = 'green'
    output = car_at_light(x)
    expected_output = 'go'
    assert output == expected_output
