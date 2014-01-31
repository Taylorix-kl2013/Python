'''
Created on 21.01.2014

@author: Marc
'''
print("How old are you?")  # print does a new_line after the output
age = input()
print("How tall are you?", end=' '),  #  " , end=' ' "  -> no new_line after print
height = input()
print("How much do you weigh?", end=' '),
weight = input()

print("So, you're %r years old, %r cm tall and %r kg heavy." % (age, height, weight))

