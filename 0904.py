# https://programmers.co.kr/learn/courses/30/lessons/12943
# 콜라츠 추측

# <문제 설명>
# - 1937년 Collatz란 사람에 의해 제기된 이 추측은, 주어진 수가 1이 될때까지 다음 작업을 반복하면, 모든 수를 1로 만들 수 있다는 추측입니다.
# - 작업은 다음과 같습니다.

# 1-1. 입력된 수가 짝수라면 2로 나눕니다. 
# 1-2. 입력된 수가 홀수라면 3을 곱하고 1을 더합니다.
# 2. 결과로 나온 수에 같은 작업을 1이 될 때까지 반복합니다.

# - 예를 들어, 입력된 수가 6이라면 6→3→10→5→16→8→4→2→1 이 되어 총 8번 만에 1이 됩니다.
# - 위 작업을 몇 번이나 반복해야하는지 반환하는 함수, solution을 완성해 주세요.
# - 단, 작업을 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.

# <제한 사항>
# - 입력된 수, num은 1 이상 8000000 미만인 정수입니다.

def solution(num):
    # 내가 짠 코드... 정확성 테스트 13이 안된다고 나온다... 왜 그런지는 모르겠다...
    # ㅠㅠ 해결했다... 정확성 테스트 13은 num은 1이었다... 
    for i in range(1, 501):
        # 테스트 케이스 13번 num = 1일 경우
        if num == 1:
            return 0
        # 짝수일 경우
        if num % 2 == 0:
            num /= 2
            if num == 1:
                return i
        # 홀수일 경우
        elif num % 2 == 1:
            num = (num * 3) + 1
            if num == 1:
                return i
    return -1

    # 다른 사람 풀이... 테스트 케이스 13번 실패가 너무 답답해서
    # 구글에 검색해서 찾은 코드이다...
    # while num != 1:
    #     # 500번 반복해도 1이 안될 경우
    #     if answer == 500:
    #         return -1
        
    #     # 짝수일 경우
    #     if num % 2 == 0:
    #         num = num / 2
    #     # 홀수일 경우
    #     else:
    #         num = num * 3 + 1
    #     answer += 1

n = 6
print(solution(n))
n = 16
print(solution(n))
n = 626331
print(solution(n))