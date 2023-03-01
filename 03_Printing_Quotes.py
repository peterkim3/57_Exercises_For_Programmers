quote = input("What is the quote? ")
author = input("Who said it? ")

# print(f'{author} says, "{quote}"')

"""
Constraints
If your language supports string interpolation or string substitution, 
don’t use it for this exercise. Use string concatenation instead.
"""

quote = '"' + quote + '"'
print(author, "says,", quote)


"""
Challenge
In Chapter 7, Data Structures, on page 63, you’ll practice working with lists of data.
Modify this program so that instead of prompting for quotes from the user, 
you create a structure that holds quotes and their associated data attributions 
and then display all of the quotes using the format in the example. 
An array of maps would be a good choice.
"""

d = {author: quote}
print(author, "says,", d[author])
