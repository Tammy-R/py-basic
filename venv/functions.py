""" 
def addition():
    a = int(input('Enter a number. '))
    b = int(input("Please enter another number. "))
    print(a + b)


addition()
"""

# Args, keywords, *args

def user_info(name, age=0, city="Novi Sad"):
    """ This function prints name, city and age
    from an argument provided to the function.
    Age and city have default values."""

    print("{} is {} years old, from {}".format(name, age, city))


user_info("Tamara", 29, "Negotin") 
user_info("Taki")
user_info(age = 30, name="Milan")

# *args & **kwargs
"""
*args allows for unlimited variables to be passed into a function without defining them ahead of time
def add(*args)
    print(sum(args))

add(2,4,6,8)

**kwargs allows for unlimikted keyword arguments to be passed into a function without defining them ahead of time
def application(**kwargs)
    print(**kwargs)

application(name="Jess", email="mail@mail.com")

Mozemo da koristimo sva 3 argumenta u funkciji, pri tome vodimo racuna da prvo unesemo definisane argumente, a onda *arg i **kwarg
"""

def application(fname, lname, email, company, *args, **kwargs):
    print("{} {} works at {}. Her/his email is {}. She works there for {} long years, {}".format(fname, lname, company, email, args, kwargs))


application("Taki", "Karanovic", "ruzictam@gmail.com", "Epam", 2, hire_date= "November 2020")
