# -*-coding:utf8
"""
참고문헌 : http://euler.synap.co.kr/prob_detail.php?id=2

피보나치 수열의 각 항은 바로 앞의 항 두 개를 더한 것이 됩니다. 1과 2로 시작하는 경우 이 수열은 아래와 같습니다.
    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
짝수이면서 4백만 이하인 모든 항을 더하면 얼마가 됩니까?

대신
4백만 이상인 최초의 항은 몇번째 얼마가 됩니까?
* Recursion 재귀함수 를 이용해 볼 수 있겠습니까?

def factorial(n):
    if 1 == n:
        return 1
else:
        return n * factorial(n - 1)

print(factorial(5))
"""


def fibonacci(n):
    if 2 == n:
        return 2
    elif 1 == n:
        return 1
    elif 0 >= n:
        return 0
    else:
        return fibonacci(n - 2) + fibonacci(n - 1)


# 여기까지 입력 후 add, commit  # 각 행 주석 입력 후 commit
