# -*- coding: cp949 -*-
# [분반] [이름] [학번]
# 참고문헌: http://learnpythonthehardway.org/book/ex4.html

# 각행 주석을 달아 보시오
cars = 100
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars - drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."

# 여기 까지 주석을 다 단 후 diff, commit

# 그 밖에 다른 study drills 항목들도 시도해 보면서 필요시 diff, commit
