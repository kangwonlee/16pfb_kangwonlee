# coding: utf-8
# 참고문헌: http://learnpythonthehardway.org/book/ex28.html

print(" 1. True and True = %s" % True and True)
print(" 2. False and True = %s" % False and True)
print(" 3. 1==1 and 2==1 = %s" % ((1 == 1) and (2 == 1)))
print(" 4. 'test' == 'test' = %s" % 'test' == 'test')
print(" 5. 1==1 or 2!=1 = %s " % ((1 == 1) or (2 != 1)))
print(" 6. True and 1==1 = %s" % True and (1 == 1))
print(" 7. False and 0!=0 = %s" % False and (0 != 0))
print(" 8. True or 1==1 = %s" % True or (1 == 1))
print(" 9. 'test' == 'testing' = %s" % 'test' == 'testing')
print("10. 1!=0 and 2==1 = %s" % (1 != 0) and (2 == 1))
print("11. 'test'!='testing' = %s" % 'test' != 'testing')
print("12. 'test'==1 = %s" % 'test' == 1)
print("13. not(True and False) = {:b}".format(not (True and False)))
print("14. not(1==1 and 0!=1) = {:b}".format(not ((1 == 1) and (0 != 1))))
print("15. not(10==1 or 1000==1000) = {:b}".format(not ((10 == 1) or (1000 == 1000))))
print("16. not(1!=10 or 3==4) = {:b}".format(not ((1 != 10) or (3 == 4))))
print("17. not('testing'=='testing' and 'Zed'=='Cool Guy') = {:b}".format(
    not (('testing' == 'testing') and ('Zed' == 'Cool Guy'))))
print("18. 1==1 and not('testing'==1 or 1==0) = {:b}".format(
    (1 == 1) and not (('testing' == 1) or (1 == 0))))
print("19. 'chunky'=='bacon' and not (3==4 or 3==3) = {:b}".format(
    ('chunky' == 'bacon') and not ((3 == 4) or (3 == 3))))
print("20. 3==3 and not('testing'=='testing' or 'Python'=='Fun') = {:b}".format(
    (3 == 3) and not (('testing' == 'testing') or ('Python' == 'Fun'))))

print("extra 1. 'test' and 'test' = = %s" % 'test' and 'test')
print("extra 2. 1 and 1 = = %s" % 1 and 1)
print("extra 3. False and 1 = = %s" % False and 1)
print("extra 4. True and 1 = = %s" % True and 1)

# 여기까지 입력 후 add, commit

# 각 행 주석 입력 후 commit

# 각자 Study drills 시도 후 필요시 commit

# 열린게시판 / 오류노트 에 각자 오류노트 작성

# 시험 문제로 만나면 곤란할 것 같은 내용은 질의응답 난에 각자 질문
# (공개 질문 추천)
