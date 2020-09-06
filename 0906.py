# https://programmers.co.kr/learn/courses/30/lessons/12937
# 짝수와 홀수

# <문제 설명>
# - 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.

# - num은 int 범위의 정수입니다.
# - 0은 짝수입니다.

# 오늘은 별거 없다...
# 2로 나누어 나머지가 1인지 0인지만 판별하면 되는 문제이다.. 쉽네 ㅋㅋ
def solution(num):
    answer = ''
    if num % 2 == 0:
        answer = 'Even'
    else:
        answer = 'Odd'

print(solution(3))
print(solution(4))