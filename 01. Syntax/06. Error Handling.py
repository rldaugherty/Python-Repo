# When programs throw errors that we didn’t expect to encounter we call those errors "bugs". Finding those bugs can be made a lot easier by using Error Handling techniques.
# 2 Types of errors we encounter are Syntax Errors and Name Errors.
# Syntax errors occur when theres a mispelling, missing punctuation or a misplaced command in your code
# Name Errors occur when Python looks for a variable or function that hasn't been defined yet.

# For example the following code will produce errors because of the mismatched quote marks (REMEMBER LESSON 4). This is considered a Syntax Error.
print('This message has mismatched quote marks!")

#This will throw an error because Abracadabra isn't a defined variable (it has no value set). This is considered a Name Error.
print(Abracadabra)