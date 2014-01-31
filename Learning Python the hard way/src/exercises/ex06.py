'''
Created on 21.01.2014

@author: Marc
'''
x = "There are %d types of people." % 10

binary = "binary"
do_not = "don't"
y = "Those who know %s and those who %s." % (binary, do_not)

print (x)
print (y)

print("I said : %r." % x)  # %r = real representation -> raw!!! good for debugging 
print("I also said: '%s' " % y)  # %s and others = representation for users.I use '' inside of strings to print them
                                                         
hilarious = False                                                                            
joke_evaluation = "Isn't that joke so funny?! %r"  # %r = call another string and format it

print(joke_evaluation % hilarious)                       

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)


