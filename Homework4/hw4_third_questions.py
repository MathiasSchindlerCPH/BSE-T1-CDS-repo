# Now imagine you have a certain data structure that
# contains information about different countries and
# the number of people who was registered with covid
# in a weekly basis.
# e.g. {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
#       'Italy': [6, 8, 1, 7]}
# Assuming that the moment they started reporting the
# number of registered cases is not the same (thus
# the length of the lists can differ)

test3 = {'Spain': [4, 8, 2, 0, 1], 'France': [2, 3, 6],
       'Italy': [6, 8, 1, 7]}

# 7)
# Create a function called "total_registered_cases"
# that has 2 parameters:
# 1) The data structure described above.
# 2) A string with the country name.
#
# The function should return the total number of cases
# registered so far
def total_registered_cases(data : dict, country : str):
    if not isinstance(data, dict) & isinstance(country, str):
        raise TypeError
    else:
        for key, val in data.items():
            if key == country:
                print(sum(val))
                
def total_registered_cases(dict_dt, country):
    total_cases = sum(dict_dt[country])
    return total_cases
            
total_registered_cases(test3, "Italy")            


# 8)
# Create a function called "total_registered_cases_per_country"
# that has 1 parameter:
# 1) The data structure described above.
#
# The function should return a dictionary with a key
# per each country and as value the total number of cases
# registered so far that the country had
def total_registered_cases_per_country(data : dict):
    if not isinstance(data, dict):
        raise TypeError
    else:
        out = {}
        for key, val in data.items():
            out[key] = sum(val)
    return out
        

def total_registered_cases_per_country(dict_dt):
    list_dict = list()
    for i in dict_dt.keys():
        list_dict.append((i, sum(dict_dt[i])))
    dict_sums = dict(list_dict)
    return dict_sums

def total_registered_cases_per_country(dict): 
    t = {}
    for k, v in dict.items():
        t[k] = sum(v)
                
    return t
                
        
total_registered_cases_per_country(test3)
        
        

# 9)
# Create a function called "country_with_most_cases"
# that has 1 parameter:
# 1) The data structure described above
#
# The function should return the country with the
# greatest total amount of cases
def country_with_most_cases(data : dict):
    if not isinstance(data, dict):
        raise TypeError
    else:
        x = total_registered_cases_per_country(data)
        x_max = max(x, key = x.get)
    return x_max

def country_with_most_cases(dict_dt):
    a = total_registered_cases_per_country(dict_dt)
    max_val = max(a.values())
    for i in a.keys():
        if a[i] == max_val:
            return i

country_with_most_cases(test3)
