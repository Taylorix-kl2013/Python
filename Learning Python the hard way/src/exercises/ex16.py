'''
Created on 21.01.2014

@author: Marc
'''
from sys import argv
# parameter = filename
script, filename = argv
print("We're going to erase %r" % filename)
print("if you don't want that,hit CTRL-C (^C)")
print("if you don't want that, hit RETURN")

input('?')

print("Opening the file...")
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
target.truncate

line1 = input("line1:")
line2 = input("line2:")
line3 = input("line3:")

print("Now I'm going to w rite these to the file.")

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print("And finally, we close it")
target.close