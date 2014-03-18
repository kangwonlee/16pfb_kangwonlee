# -*- coding: cp949 -*-
import re
# regular expression

f = open("140318pfa.txt", 'r')
txt = f.read()
f.close()

# done reading file

# '@dev.naver.com/' 와 같은 문자열을 포함하고 앞뒤로 다른 글자가 있는 모든 행을
# txt 에서 찾는
found = re.findall(".+@dev.naver.com/.+", txt)

for item in found:
    print item
