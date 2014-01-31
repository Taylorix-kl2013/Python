'''
Created on 30.01.2014

@author: Marc
'''
from sys import argv


script, from_file, to_file = argv

print("Copying from %s to %s" % (from_file, to_file) )

# we could do these two steps on one line too, how?
in_file = open(from_file)
indata = in_file.read()
out_file = open(to_file, 'w')

print("The input file is %d bytes long" % len(indata))

out_file = open(to_file, 'w')
out_file.write(indata)
print("Alright, all done.")


out_file.close()
in_file.close()