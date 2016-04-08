# -*- coding: utf8 -*-
# http://learnpythonthehardway.org/book/ex13.html
from sys import argv

print("argv = " + str(argv))
script, first, second = argv

print("The script is called: %s" % script)
print("Your first variable is : %s" % first)
print("Your second variable is : %s" % second)
