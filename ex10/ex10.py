# -*- coding: utf8 -*-
# http://learnpythonthehardway.org/book/ex10.html
# 한글주석
tabby_cat = "\tI'm tabbed in. 한글출력"
space_cat = "    I'm tabbed in. 한글출력"
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(space_cat)
print(persian_cat)
print(backslash_cat)
print('Study Drills 10.05\n %r' % fat_cat)
