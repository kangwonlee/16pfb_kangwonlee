print("Mary had a little lamb.")
print("Its fleece was white as %s." % 'snow')
print("And everywhere that Mary went.")
print("." * 10)  # what'd that do?
print("1234567890"*6)

end01 = "C"
end02 = "h"
end03 = "e"
end04 = "e"
end05 = "s"
end06 = "e"
end07 = "B"
end08 = "u"
end09 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch that comma at the end. try removing it to see what happens
# Python 2.7
print end01 + end02 + end03 + end04 + end05 + end06,
# Python 3.x
# print(end01 + end02 + end03 + end04 + end05 + end06, end=' ')
print(end07 + end08 + end09 + end10 + end11 + end12)
