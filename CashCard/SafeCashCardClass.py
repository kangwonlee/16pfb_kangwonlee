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
        # 잔고가 충분하면
        if self.check_balance() >= amount_won:
            # 출금한다
            # 상위 클래스의 withdraw 메소드 호출
            # http://stackoverflow.com/questions/805066/
            CashCard.withdraw(self, amount_won)
        # 그렇지 않으면
        else:
            # 오류를 표시한다
            print("** 오류 발생 **")
            print("잔고가 부족합니다")
            print("인출되지 않았습니다")

# SafeCashCard 클래스 정의 끝
