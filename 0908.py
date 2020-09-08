# https://programmers.co.kr/learn/courses/30/lessons/12934
# 정수 제곱근 판별

# <문제 설명>
# - 임의의 양의 정수 n에 대해, n이 어떤 양의 정수 x의 제곱인지 아닌지 판별하려 합니다.
# - n이 양의 정수 x의 제곱이라면 x+1의 제곱을 리턴하고, n이 양의 정수 x의 제곱이 아니라면 -1을 리턴하는 함수를 완성하세요.

# <제한 사항>
# - n은 1이상, 5000000000000000 이하인 양의 정수입니다.

# 나도 드디어 2줄 코딩... 다음에는 한줄 코딩해야지~~ㅋㅋ
def solution(n):
    # n에 루트를 씌어 계산한 결과값이 n이다.
    # n의 타입은 float이다.
    n **= 0.5
    return int(( n + 1 ) ** 2) if n % 1 == 0 else -1

print(solution(121))
print(solution(3))