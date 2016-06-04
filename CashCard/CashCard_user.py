# -*- coding:utf8 -*-

# 현금 카드 모듈을 불러들임
import CashCard as CashCard_module


def chk_bal(message, account):
    """
    Print message and value
    :param message:
    :param account:
    :return:
    """
    print("%s : %d" % (message, account.check_balance()))


# 현금 카드 모듈의 잔액 확인
chk_bal("CashCard_module 잔액확인", CashCard_module)
# 현금 카드에 10000원 입금
print("10000원 입금")

# CashCard.py 모듈 안의 deposit() 함수를 호출
# CashCard.py 모듈 안의 balance_won 값이 증가
CashCard_module.deposit(10000)

# CashCard.py 모듈 안의 check_balance() 함수를 호출
#   CashCard.py 모듈 안의 balance_won 값을 반환
chk_bal("입금 후 잔고 확인", CashCard_module)

print("1000원 출금")
# CashCard.py 모듈 안의 withdraw() 함수를 호출
# CashCard.py 모듈의 balance_won 값이 감소
CashCard_module.withdraw(1000)

# Cash Card 모듈 안의 check_balance() 함수롤 호출
#   CashCard.py 모듈 안의 balance_won 값을 반환
chk_bal("출금 후 잔고 확인", CashCard_module)

# 또 다른 현금 카드를 만들 수 있을까? 불러 들임
# noinspection PyPep8
import CashCard as mySistersCard_module

chk_bal("CashCard_module 잔액 확인", CashCard_module)
chk_bal("mySistersCard_module 잔액 확인", mySistersCard_module)

# 그러나 이런 식으로는 한 장의 카드만 만들 수 있다
print("CashCard_module : %s" % CashCard_module)
print("mySistersCard_module : %s" % mySistersCard_module)
