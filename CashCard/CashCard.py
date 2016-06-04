# -*- coding:utf8 -*-
balance_won = 0  # 현금 카드 잔고


# 현금 카드로 할 수 있는 것: 입금, 출금, 잔고확인

def deposit(amount_won):
    """
    Deposit some amount of money into cash card
    :param amount_won:
    :return:
    """
    # deposit 함수 안의 balance_won 이
    # 전역 변수 임을 표시
    global balance_won

    # 입금하면 잔고가 증가한다
    balance_won += amount_won


def withdraw(amount_won):
    """
    Withdraw some amount of money from cash card
    :param amount_won:
    :return:
    """
    # withdraw 함수 안의 balance_won 이
    # 전역 변수임을 표시
    global balance_won

    # 출금하면 잔고가 감소한다
    balance_won += (-amount_won)


def check_balance():
    """
    Check how much money is in the cash card
    :return:
    """
    # 통장 잔고를 반환한다
    # reader function
    return balance_won
