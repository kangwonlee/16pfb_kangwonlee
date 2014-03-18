# -*- coding: cp949 -*-
# [분반] [이름] [학번]
# 참고문헌: http://learnpythonthehardway.org/book/ex5.html

# 각행 주석을 달아 보시오

my_name = 'Kangwon Lee' # 각자 자신의 이름
my_age = 25 # a lie
my_height_cm = 180 # also a lie in centimeters
my_weight_kg = 70 # 변수명에는 단위 명기 바람
my_eyes = "Brown" # 동양인은 대부분 갈색
my_teeth = "White"
my_hair = 'Brown'

print "Let's talk about %s." % my_name
# He -> She if appropriate
print "He's %d centimeters tall." % my_height_cm
print "He's %d kilograms heavy." % my_weight_kg
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % ( my_eyes, my_teeth )
print "His teeth are usually %s depending on the coffee." % my_teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (
    my_age, my_height_cm, my_weight_kg, my_age + my_height_cm + my_weight_kg)

# 여기 까지 주석을 다 단 후 diff, commit

# 그 밖에 다른 study drills 항목들도 시도해 보면서 필요시 diff, commit
