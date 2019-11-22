#Python strings are very flexible, but if we try to create a string that occupies multiple lines we find ourselves face-to-face with a SyntaxError. Python offers a solution: multi-line strings. By using three quote-marks (""" or ''') instead of one, we tell the program that the string doesn’t end until the next triple-quote. 

# Assign the string here
to_you = """Stranger, if you passing meet me and desire to speak to me, why
  should you not speak to me?
And why should I not speak to you?"""

print(to_you)