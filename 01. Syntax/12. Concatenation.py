#Concatenating is stringing 2 or more variables together. Even though it uses the "+" operator, it's simply adding the strings to each other. It's VERY IMPORTANT to note that the strings MUST be in quotes, and this includes numbers. If you try to concatenate a number without quotes to a string, it will throw a TypeError error

string1 = "The wind, "
string2 = "which had hitherto carried us along with amazing rapidity, "
string3 = "sank at sunset to a light breeze; "
string4 = "the soft air just ruffled the water and "
string5 = "caused a pleasant motion among the trees as we approached the shore, "
string6 = "from which it wafted the most delightful scent of flowers and hay."

# Define message below:
message = string1+string2+string3+string4+string5+string6

#print(message)
print(message)