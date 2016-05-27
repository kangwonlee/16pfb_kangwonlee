# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex39.html
# http://eclass.kpu.ac.kr/ilos/pf/course/lecture_material_view_form.acl?ARTL_NUM=373489&SCH_KEY=&SCH_VALUE=&display=10&start=1
import hashmap

# create a mapping fo states to abbreviation
states = hashmap.new()
hashmap.set(states, 'Oregon', 'OR')
hashmap.set(states, 'Florida', 'FL')
hashmap.set(states, 'California', 'CA')
hashmap.set(states, 'New York', 'NY')
hashmap.set(states, 'Hawaii', 'HI')

# create a basic set of states and some cities in them
cities = hashmap.new()
hashmap.set(cities, 'CA', 'Los Angeles')
hashmap.set(cities, 'HI', 'Honolulu')
hashmap.set(cities, 'FL', 'Orlando')

# add some more cities
hashmap.set(cities, 'NY', 'New York')
hashmap.set(cities, 'OR', 'Portland')

# print out some cities
print('-' * 10)
print("NY State has: %s" % hashmap.get(cities, 'NY'))
print("HI State has: %s" % hashmap.get(cities, 'HI'))

# print some states
print('-' * 10)
print("Hawaii's abbreviation is: %s" % hashmap.get(states, 'Hawaii'))
print("Florida's abbreviation is: %s" % hashmap.get(states, 'Florida'))

# do it by using the state then cities dict
print('-' * 10)
print('Hawaii has: %s' % hashmap.get(cities, hashmap.get(states, 'Hawaii')))
print('Florida has: %s' % hashmap.get(cities, hashmap.get(states, 'Florida')))

# print every state abbreviation
print('-' * 10)
hashmap.list(states)

# print every city in state
print('-' * 10)
hashmap.list(cities)

# 입력 후 add, commit  # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit

#  오류노트 에 각자 오류노트 작성
