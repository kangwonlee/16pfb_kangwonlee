# -*- coding: cp949 -*-
# [분반] [학번] [이름]
# ref : http://learnpythonthehardway.org/book/ex8.html

formatter = "%r %r %r %r"
formatter2 = '%s %s %s %s'

print formatter % (1, 2, 3, 4)
print formatter % ("하나", "둘", "셋", "넷")
print formatter2 % ("하나", "둘", "셋", "넷")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
    )
 
# 여기까지 입력 후 add, commit

# 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit

# 열린게시판 / 오류노트 에 각자 오류노트 작성
