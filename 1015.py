# https://programmers.co.kr/learn/courses/30/lessons/12924
# 숫자의 표현

# <문제 설명>
# - Finn은 요즘 수학공부에 빠져 있습니다.
# - 수학 공부를 하던 Finn은 자연수 n을 연속한 자연수들로 표현 하는 방법이 여러개라는 사실을 알게 되었습니다.
# - 예를들어 15는 다음과 같이 4가지로 표현 할 수 있습니다.
#   - 1 + 2 + 3 + 4 + 5 = 15
#   - 4 + 5 + 6 = 15
#   - 7 + 8 = 15
#   - 15 = 15
# 자연수 n이 매개변수로 주어질 때, 연속된 자연수들로 n을 표현하는 방법의 수를 return하는 solution를 완성해주세요.

# 제한사항
# n은 10,000 이하의 자연수 입니다.

# 힌트에서 등차수열의 합을 이용해 푼다고 한다...
def solution(n):
    # n은 등차수열에서 항의 개수
    # a는 첫째항
    answer = 0
    for i in range(1, n//2+1):
        tmp_sum = 0
        for j in range(i, n+1):
            tmp_sum += j
            if tmp_sum == n:
                answer += 1
            elif tmp_sum > n:
                break
    return answer + 1

# 이걸 어떻게 알았을까??
# def solution(num):
#     return [i  for i in range(1,num+1,2) if num % i == 0]
# 예를 들어 n이 3개의 연속된 자연수(i-1, i, i+1)의 합으로 표현된다면 합은 3i가 됩니다.
# 즉, n은 3의 배수입니다.
# 마찬가지로 5개의 연속된 자연수의 합으로 n이 표현이 된다면 n은 5의 배수여야합니다.
# 따라서, n의 약수 중 홀수가 몇개있냐는 문제와 같은 문제로 해석할 수 있습니다.

print(solution(15))