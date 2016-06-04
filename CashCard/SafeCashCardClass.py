# -*- coding:utf8 -*-
# 상위 클래스 이름이 너무 길 경우 from import as 로 줄일 수 있음
from CashCardClass import SimpleCashCard as CashCard


# Cash Card Class 모듈의 SimpleCashCard 클래스를
# 상속받아 SafeCashCard 클래스를 정의한다
# SimpleCashCard 는 SafeCashCard 의 상위 클래스
# SafeCashCard 는 SimpleCashCard 의 하위 클래스
class SafeCashCard(CashCard):
    # SimpleCashCard 의 다른 기능은 그대로 사용하고
    #       {__init__(), deposit(), check_balance()}
    #   withdraw() 메소드만 다시 정의한다
    def withdraw(self, amount_won):
        """
        SafeCashCard withdraw method
        Check balance before withdraw
        :param amount_won:
        :return:
        """
        print("SafeCashCard withdraw()")  # 함수 호출 표식
