# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex47.html
# 각 행 주석 입력

from nose.tools import *

from game import Room


def test_room():
    gold = Room("GoldRoom",
                """This room has gold in it you can grab. There's a
door to the north.""")

    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})


def test_room_paths():
    center = Room("Center", "Test room in the center.")
    north = Room("North", "Test room in the north.")
    south = Room("North", "Test room in the south.")

    center.add_paths({'north': north, 'south': south})

    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)


# 입력 후 add, commit

# 각자 Study drills 시도 후 필요시 commit

#  오류노트 에 각자 오류노트 작성
