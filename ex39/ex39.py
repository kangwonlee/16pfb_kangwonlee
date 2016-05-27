# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex39.html

# create a mapping of state to abbreviation
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Hawaii': 'HI',
}

# create a basic set of states and some cities in them
cities = {
    'CA': 'San Francisco',
    'HI': 'Honolulu',
    'FL': 'Jacksonville',
}

# add some more cities
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# print out some cities
print('-' * 10)
print('NY State has: %s' % cities['NY'])
print('OR State has: %s' % cities['OR'])

# print some states
print('-' * 10)
print("Hawaii's abbreviation is: %s" % states['Hawaii'])
print("Florida's abbreviation is: %s" % states['Florida'])

# print every state abbreviation
print('-' * 10)
print("states = %s" % states)
print("states.items() = %s" % str(states.items()))
print('-' * 10)
for state, abbrev in states.items():
    print("%s is abbreviated %s" % (state, abbrev))

# print every city in state
print('-' * 10)
for abbrev, city in cities.items():
    print("%s has the city %s" % (abbrev, city))

# now do both at the same time
print('-' * 10)
for state, abbrev in states.item():
    print("%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev]
    ))


# 입력 후 add, commit  # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit  # 오류노트 에 각자 오류노트 작성
