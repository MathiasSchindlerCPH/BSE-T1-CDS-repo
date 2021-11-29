# 3)
# Imagine you have a dictionary with the attributes of a person
# {'name': 'John', 'last_name': 'Doe', 'birth': 1987}
# {'name': 'Janet', 'last_name': 'Bird', 'gender': 'female'}
# create two functions that returns the age of the person
# that handles both examples.
# Name the first function "retrieve_age_eafp" and follow EAFP
# Name the second function "retrieve_age_lbyl" and follow lbyl

def test_retrieve_age_eafp():
    x = {'name': 'Meryl', 'last_name': 'Streep', 'birth': 1949}
    output = retrieve_age_eafp(x)
    expected_output = 'Meryl Streep is 72 years old'
    assert output == expected_output
    
    
def test_retrieve_age_lbyl():
    x = {'name': 'Will', 'last_name': 'Smith', 'birth': 1968}
    output = retrieve_age_lbyl(x)
    expected_output = 'Will Smith is 53 years old'
    assert output == expected_output