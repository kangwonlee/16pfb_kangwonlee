# -*- coding: utf8 -*-
# http://learnpythonthehardway.org/book/ex13.html
from sys import argv

print("argv = " + str(argv))
script, first, second, third, fourth = argv

print("The script is called: %s" % script)
print("Your first variable is : %s" % first)
print("Your second variable is : %s" % second)
print("Your third variable is : %s" % third)
print("Your fourth variable is : %s" % fourth)
