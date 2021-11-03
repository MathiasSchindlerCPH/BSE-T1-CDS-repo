# Now, imagine you are given data from a website that
# has people's CVs. The data comes
# as a list of dictionaries and each
# dictionary looks like this:
#
# { 'user': 'george', 'jobs': ['bar', 'baz', 'qux']}
# e.g. [{'user': 'john', 'jobs': ['analyst', 'engineer']},
#       {'user': 'jane', 'jobs': ['finance', 'software']}]
# we will refer to this as a "CV".
#


test2 = [{'user': 'john', 'jobs': ['analyst', 'engineer']},
       {'user': 'jane', 'jobs': ['engineer', 'software']}]


#
# 4)
# Create a function called "has_experience_as"
# that has two parameters:
# 1. A list of CV's.
# 2. A string (job_title)
#
# The function should return a list of strings
# representing the usernames of every user that
# has worked as job_title.

def has_experience_as(cv: list, job_title: str):
    if not isinstance(cv, list) & isinstance(job_title, str) :
        raise TypeError
    else:
        user_has_worked = []
        for i in range(len(cv)):
            for key, val in cv[i].items():
               if isinstance(val, list):
                   for val in val:
                       if val == job_title:
                           x = cv[i]["user"]
                           user_has_worked.append(x)
    return user_has_worked
    
def has_experience_as(cv, job_title):
    name_with_job = list()
    for i in range(len(cv)):
        if job_title in cv[i]['jobs']:
            name_with_job.append(cv[i]['user'])
    
    if len(name_with_job) == 0:
        print('There is no any user with experience in', job_title)
    else:
        return name_with_job   
#
# 5)
# Create a function called "job_counts"
# that has one parameter: list of CV's
# and returns a dictionary where the
# keys are the job titles and the values
# are the number of users that have done
# that job.

def job_counts(cv: list):
    if not isinstance(cv, list):
        raise TypeError
    else:
        temp = []
        for i in range(len(cv)):
            for keys, val in cv[i].items():
                if isinstance(val, list):
                    for val in val:
                        temp.append(val)
        count = collections.Counter(temp)
    return count



job_counts(test2)
            


# 6)
# Create a function, called "most_popular_job"
# that has one parameter: a list of CV's, and
# returns a tuple (str, int) that represents
# the title of the most popular job and the number
# of times it was held by people on the site.
#
# HINT: You should probably use your "job_counts"
# function!
#
# HINT: You can use the method '.items' on
# dictionaries to iterate over them like a
# list of tuples.
def most_popular_job(cv: list):
    if not isinstance(cv, list):
        raise TypeError
    else:
        x = job_counts(cv)
        x_max_key = max(x, key = x.get)
        x_max_val = max(x.values())
        result = (x_max_key, x_max_val)
    return result

xx = most_popular_job(test2)
type(xx)    #tuple
type(xx[0]) #str
type(xx[1]) #int


def most_popular_job(listofcv):
    a = job_counts(listofcv)
    max_val = max(a.values())
    for i in a.keys():
        if a[i] == max_val:
            return (i, a[i])
    
