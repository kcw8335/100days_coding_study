# https://programmers.co.kr/learn/courses/30/lessons/12921
# 소수 찾기

# <문제 설명>
# - 1부터 입력받은 숫자 n 사이에 소수의 개수를 반환하는 함수, solution을 만들어 보세요.
# - 소수는 1과 자기 자신으로만 나누어지는 수를 의미합니다.
# - 1은 소수가 아닙니다.

# <제한 조건>
# - n은 2이상 1000000이하의 자연수입니다.

# 소수인지 아닌지 판별하는 함수
import math
def prime_number_discriminant_function(number):
    # 시간을 줄이기 위해 number의 제곱근까지만 반복
    how_many = int(math.sqrt(number)) + 1
    for i in range(2, how_many):
        # 소수는 자기 자신으로만 나누어지는 수
        # 다른 수랑 나누어지면 소수가 아님
        if number % i == 0:
            return False
    return True
        

def solution(n):
    answer = 0
    for i in range(2, n+1):
        if prime_number_discriminant_function(i):
            answer += 1
    return answer


print(solution(10))
print(solution(5))