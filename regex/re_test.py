# -*- coding: cp949 -*-
import re

f = open("repo_list.txt", 'r')
txt = f.read()
f.close()

# regular expression 을 이용하여 관심 문자열을 찾음
found = re.findall("https://.+[/,](.+).git", txt)
print "len(found) =", len(found)
while found:
    item = found.pop()
    print item, 
    print "\t[ duplicate =", item in found, ']'
