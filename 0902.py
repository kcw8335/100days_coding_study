# https://programmers.co.kr/learn/courses/30/lessons/12947
# 하샤드 수

# <문제 설명>
# - 양의 정수 x가 하샤드 수이려면 x의 자릿수의 합으로 x가 나누어져야 합니다.
# - 예를 들어 18의 자릿수 합은 1+8=9이고, 18은 9로 나누어 떨어지므로 18은 하샤드 수입니다. 
# - 자연수 x를 입력받아 x가 하샤드 수인지 아닌지 검사하는 함수, solution을 완성해주세요.

# <제한 조건>
# - x는 1 이상, 10000 이하인 정수입니다.

def solution(x):
    # 내가 푼 풀이...ㅠㅠ
    # sum, tmp = 0, x
    # for i in range(len(str(x))):
    #     sum += (x % 10)
    #     x //= 10    
    # return True if tmp % sum == 0 else False

    # 다른 사람 풀이
    return x % sum([int(c) for c in str(x)]) == 0

x = 10
print(solution(x))
x = 12
print(solution(x))
x = 11
print(solution(x))
x = 13
print(solution(x))
