# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex38.html
ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait there are not 10 things in that list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee", "Corn", "Banana", "Girl", "Boy"]

while (len(stuff)) != 10:
    next_one = more_stuff.pop()
    print("Adding: %s" % next_one)
    stuff.append(next_one)
    print("There are %d items now." % len(stuff))

print("There we go :%s" % str(stuff))
print("Let's do some things with stuff")

print("stuff[1] = %s" % stuff[1])
print("stuff[-11] = %s" % stuff[-1])
print("stuff.pop() = %s" % stuff.pop())
print(' '.join(stuff))
print('#'.join(stuff[3:5]))

# 입력 후 add, commit  # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit  # 오류노트 에 각자 오류노트 작성
