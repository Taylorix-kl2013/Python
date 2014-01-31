'''
Created on 21.01.2014

@author: Marc
'''
#===============================================================================
# import other libraries | argv = argument variable
# holds the arguments you want to pass to your script
#===============================================================================
from sys import argv            
#==============================================================================
# assigns the passed arguments to variables       
#==============================================================================
script, first, second, third = argv     

print("The script is called:", script)
print("Your first variable is:", first)
print("your second variable is:", second)
print("Your third variable is", third)
