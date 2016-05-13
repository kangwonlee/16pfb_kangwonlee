# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex32.html

i = 0
numbers = []

while i < 6:
    print("At the top i is %d" % i)
    numbers.append(i)

    i = i + 1

    print("Numbers now: " + str(numbers))
    print("At the bottom i is %d" % i)

print("The numbers: ")

for num in numbers:
    print(num)

# 여기까지 입력 후 add, commit  # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit  # 오류노트 에 각자 오류노트 작성
