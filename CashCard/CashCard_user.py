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
chk_bal("CashCard_module 잔액확인".CashCard_module)
# 현금 카드에 10000원 입금
print("10000원 입금")

# CashCard.py 모듈 안의 deposit() 함수를 호출
# CashCard.py 모듈 안의 balance_won 값이 증가
CashCard_module.deposit(10000)
