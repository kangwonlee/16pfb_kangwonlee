# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex30.html

people = 30
cars = 40
trucks = 15

if cars > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide")

if people > trucks:
    print("Alright, let's just take the trucks.")
else:
    print("Fine, let's stay home then.")

# 여기까지 입력 후 add, commit

# 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit

# 오류노트 에 각자 오류노트 작성
