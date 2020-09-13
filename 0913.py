# https://programmers.co.kr/learn/courses/30/lessons/12928
# 약수의 합

# <문제 설명>
# - 정수 n을 입력받아 n의 약수를 모두 더한 값을 리턴하는 함수, solution을 완성해주세요.

# <제한 사항>
# - n은 0이상 3000이하인 정수입니다.

# 드디어 한줄 코딩 성공ㅋㅋㅋㅋㅋ
def solution(n):
    # sum함수에 int형 리스트가 들어가면 다 더해진 int형이 return 된다.
    # for문의 성능을 높이기 위해 n을 2로 나눈 범위까지만 반복을 진행하고 마지막에 자기자신을 더해주었다.
    return sum([i for i in range(1, (n//2) + 1) if n % i == 0]) + n

print(solution(12))
print(solution(5))