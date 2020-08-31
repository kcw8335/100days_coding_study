# https://programmers.co.kr/learn/courses/30/lessons/12954
# x만큼 간격이 있는 n개의 숫자

# <문제 설명>
# - 함수 solution은 정수 x와 자연수 n을 입력 받아, x부터 시작해 x씩 증가하는 숫자를 n개 지니는 리스트를 리턴해야 합니다.
# - 다음 제한 조건을 보고, 조건을 만족하는 함수, solution을 완성해주세요.

# <제한 조건>
# - x는 -10000000이상, 10000000 이하인 정수 입니다.
# - n은 1000이하인 자연수 입니다.

def solution(x, n):
    answer = []
    # 증가해야 하는 초기값 변수 선언
    initial_value = x
    # 초기값에 얼만큼 증가해야 하는지를 알려주는 증가 변수 선언
    increase_value = x
    # 반복문을 사용
    for i in range(0, n):
        # 초기값을 answer 리스트에 추가
        answer.append(initial_value)
        # 초기값을 증가값만큼 증가시킨 후 다시 초기변수에 저장
        initial_value += increase_value
    return answer

x = 2
n = 5
print(solution(x, n))

x = 4
n = 3
print(solution(x, n))

x = -4
n = 2
print(solution(x, n))
