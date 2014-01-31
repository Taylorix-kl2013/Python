'''
Created on 21.01.2014

@author: Marc
'''
tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\ a \\ cat"


fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""


print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# some escape sequences
print(" \" \' \a\b\f\n\r\t\v\ooo ")
# prints an ASCII Character with the input hex value
print("\x22")

while True:
    for i in ["/", "-", "|", "\\", "|"]:
        print("%s\r" % i)
