# -*- coding:utf8 -*-
class SimpleCashCard:
    """
    SimpleCashCard class
    deposit, withdraw, and check_balance methods
    """

    def __init__(self):
        print("SimpleCashCard __init__()")  # 함수 호출 표식
        # 클래스 생성자 (컨스트럭터)
        # 멤버 변수 초기화
        # 각 카드 별로 따로 잔고를 기록한다
        self.balance_won = 0

    # 메소드 methods : # 객체에 어떤 신호를 전달하는 역할을 한다
    def deposit(self, amount_won):
        """
        입금
        :param amount_won:입금액수
        :return:
        """
        print("SimpleCashCard deposit()")  # 함수 호출 표식
        # 입금하면 잔고가 증가한다
        self.balance_won += amount_won

    def withdraw(self, amount_won):
        """
        출금
        :param amount_won: 출금액수
        :return:
        """
        print("SimpleCashCard withdraw()")  # 함수 호출 표식
        # 출금하면 잔고가 감소한다
        self.balance_won += (-amount_won)

    def check_balance(self):
        """
        잔고조회
        :return:
        """
        print("SimpleCashCard check_balance()")  # 함수 호출 표식
        # 통장 잔고를 반환한다
        return self.balance_won

# SimpleCashCard 클래스 정의 끝
