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

# 아래의 내용은 이 파일이 import 될 때는 실행되지 않음
if '__main__' == __name__:
    # 모듈 실습 함수를 하나 사용할 수 있게 함
    from CashCard_user import chk_bal

    # myCard 객체를 생성한다
    #   SimpleCashCard 클래스에 정한 대로 만든다
    #   SimpleCashCard __init__() 메소드가 호출된다
    myCard = CashCard()
    # mySafeCard 객체를 생성한다
    #   SafeCashCard 클래스에 정한 대로 만든다
    #   SafeCashCard __init__() 메소드를 호출하려고 하지만
    #   SafeCashCard 클래스 안에는 정의되지 않았기 때문에
    #   상위 클래스인 SimpleCashCard __init__() 메소드가 호출된다
    mySafeCard = SafeCashCard()

    # 여러장의 카드를 생성할 수 있는지 확인하기 위해 객체를 하나 더
    mySistersSafeCard = SafeCashCard()

    # 카드에 각각 만원씩 입금
    #   SimpleCashCard 클래스의 deposit() 메소드가 호출된다
    myCard.deposit(10000)
    #   SafeCashCard deposit() 메소드를 호출하려고 하지만
    #   SafeCashCard 클래스 안에는 정의되지 않았기 때문에
    #   상위 클래스인 SimpleCashCard 의 deposit() 메소드가 호출된다
    mySafeCard.deposit(10000)
    mySistersSafeCard.deposit(200000)

    chk_bal("myCard 입금 후 잔고 확인", myCard)
    chk_bal("mySafeCard 입금 후 잔고 확인", mySafeCard)
    chk_bal("mySistersSafeCard 입금 후 잔고 확인", mySistersSafeCard)
    #   SafeCashCard check_balance() 메소드를 호출하려고 하지만
    #   SafeCashCard 클래스 안에는 정의되지 않았기 때문에
    #   상위 클래스인 SimpleCashCard 의 check_balance() 메소드가 호출된다
