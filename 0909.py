# https://programmers.co.kr/learn/courses/30/lessons/12933
# 정수 내림차순으로 배치하기

# <문제 설명>
# - 함수 solution은 정수 n을 매개변수로 입력받습니다.
# - n의 각 자릿수를 큰 것부터 작은 순으로 정렬한 새로운 정수를 리턴해주세요.
# - 예를 들어 n이 118372면 873211을 리턴하면 됩니다.

# <제한 조건>
# - n은 1이상 8000000000이하인 자연수 입니다.

def solution(n):
    # 나의 문제 풀이
    # answer = 0
    # arr = list()
    # # n 매개변수를 int형 list로 변환
    # for i in str(n):
    #     arr.append(int(i))
    # for i in range(0, len(arr)):
    #     answer = (answer + max(arr)) * 10
    #     arr.remove(max(arr))
    # return answer // 10

    # 다른 사람 문제 풀이 - 내장함수를 잘 사용했다... 알아갈게 많네...
    arr = list(str(n))
    arr.sort(reverse = True)
    return int("".join(arr))

print(solution(118372))