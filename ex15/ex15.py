# -*-coding:cp949
# http://learnpythonthehardway.org/book/ex15.html
from sys import argv

script, filename = argv

txt = open(filename)

print("Here's your file %r:" % filename)
print(txt.read())

print("Type the filename again:")
file_again = raw_input("> ")
# python 3 : file_again = input("> :)

txt_again = open(file_again)

print(txt_again.read())
