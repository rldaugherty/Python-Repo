#You can define variables outside the scope of the funtion and still use them inside the function, for example 'current_year'
current_year = 2048

#when you do this, you only have to pass the 'birth_year' value as the function argument. You do this by using "calculate_age([value])".
def calculate_age(birth_year):
    age = current_year - birth_year
    return age
#using the print statment here, it prints the value of the returned function, or the value of "age" as in this example.
print(calculate_age(1970))