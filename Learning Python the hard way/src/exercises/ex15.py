'''
Created on 21.01.2014

@author: Marc
'''
from sys import argv
# parameter = filename
script, filename = argv
#assigns the method open() to the object 'txt'
txt = open(filename)
#prints the filename and the content of the file
print("Here is your file %r" % filename)
#calls the function .read() on the opened file
print (txt.read())

print("Type the filename again.")
file_again = input(">")
#assigns the method open() to the object 'txt_again'
txt_again = open(file_again)
#calls the function .read() on the opened file
print(txt_again.read())
txt_again.close
txt.close