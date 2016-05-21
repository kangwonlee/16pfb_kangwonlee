# -*-coding:utf8
# http://learnpythonthehardway.org/book/ex35.html
from sys import exit

if "raw_input" not in dir(__builtins__):
    raw_input = input


def gold_room():
    print("This room is full of gold. How much do you take?")

    choice = raw_input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice, you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move th bear?")
    bear_moved = False

    while True:
        choice = raw_input("> ")

        if "take honey" == choice:
            dead("The bear looks at you then slaps your face off.")
        elif "taunt bear" == choice and not bear_moved:
            print("The bear has moved from the door. You can go through it now.")
            bear_moved = True
        elif "taunt bear" == choice and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares you and you go insane.")
    print("Do you flee for your life or eat your head?")

    choice = raw_input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()


def dead(why):
    print("%s, Good job!" % why)
    exit(0)


def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")

    choice = raw_input("> ")

    if "left" == choice:
        bear_room()
    elif "right" == choice:
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")


if __name__ == '__main__':
    start()

# 여기까지 입력 후 add, commit  # 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit  # 오류노트 에 각자 오류노트 작성
