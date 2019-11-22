#The first type we’re going to learn about is the “integer type” of variable. This type stores only numeric information. You can set these in 1 of 2 ways, as a whole number or as a decimal.

#To set the value as a whole number, you can simply use “my_variable = int(my_value)“. Using the “int()” function takes your supplied number, and tells python to make sure to keep this as a number value. Be careful though, because trying to pass a non-numeric number or a decimal number to the “int()” function will cause Python to “throw” and error, so only use numbers like “10” & “85”, not “ten” and “eighty-five” or even “85.1”!

#If you do want to set the value to “85.1”, you don’t want to use the “int()” function. Instead, you’ll want to use the “float()” function. This tells Python that somewhere in the number you’re going to pass, there could be a decimal floating around there somewhere, so be prepared for it. To pass the decimal value of a number to a variable, use “my_variable = float(my_value)“. It’s the “float” function that makes this so important. This allows us to use the variable in math equations that may result in a decimal point being returned.

# Define the release and runtime integer variables below:
release_year = 1994
runtime = 120

# Define the rating_out_of_10 float variable below: 
rating_out_of_10 = float(9.8)