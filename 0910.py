# https://programmers.co.kr/learn/courses/30/lessons/12932
# 자연수 뒤집어 배열로 만들기

# <문제 설명>
# - 자연수 n을 뒤집어 각 자리 숫자를 원소로 가지는 배열 형태로 리턴해주세요.
# - 예를 들어 n이 12345이면 [5,4,3,2,1]

# <제한 조건>
# - n은 10,000,000,000이하인 자연수입니다.

def solution(n):
    # 내가 푼 문제풀이
    # n이라는 자연수를 string으로 변환하고 list의 각 원소를 map함수를 이용해서 int형으로 변환
    answer = list(map(int, list(str(n))))
    # answer이라는 리스트를 reverse함수를 이용해서 뒤집음
    answer.reverse()
    return answer

    # 다른 사람 문제풀이
    # reversed함수를 이용해서 string을 변환해주고 변환을 진행했다... 
    # 나는 list를 reverse할 생각을 해서... 2줄 코딩이 되었다... 이렇게 1줄 코딩 가능한 것을...
    # return list(map(int, reversed(str(n))))


print(solution(12345))