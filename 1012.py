# https://programmers.co.kr/learn/courses/30/lessons/12945
# 피보나치 수

# <문제 설명>
# - 피보나치 수는 F(0) = 0, F(1) = 1일 때, 1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

# - 예를들어
#   - F(2) = F(0) + F(1) = 0 + 1 = 1
#   - F(3) = F(1) + F(2) = 1 + 1 = 2
#   - F(4) = F(2) + F(3) = 1 + 2 = 3
#   - F(5) = F(3) + F(4) = 2 + 3 = 5
# - 와 같이 이어집니다.

# 2 이상의 n이 입력되었을 때, n번째 피보나치 수를 1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

# <제한 사항>
# * n은 1이상, 100000이하인 자연수입니다.

# 맨 처음에는 재귀함수로 풀었다...
# 그런데 100이상부터 호출되는 함수가 너무 많아진다... 런타임 에러 및 시간 초과가 나온다...
# 그래서 반복문을 사용해서 풀었는데... 빠르다... 재귀함수로 풀었다고 좋아했는데...
def solution(n):
    tmp_list = [0] * (n+1)
    tmp_list[1] = 1
    for i in range(2, len(tmp_list)):
        tmp_list[i] = (tmp_list[i-1] + tmp_list[i-2]) % 1234567
    return tmp_list[n]

print(solution(3))
print(solution(5))