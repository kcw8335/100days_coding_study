# https://programmers.co.kr/learn/courses/30/lessons/12940
# 최소공배수와 최대공약수

# <문제 설명>
# - 두 수를 입력받아 두 수의 최대공약수와 최소공배수를 반환하는 함수, solution을 완성해 보세요.
# - 배열의 맨 앞에 최대공약수, 그다음 최소공배수를 넣어 반환하면 됩니다.
# - 예를 들어 두 수 3, 12의 최대공약수는 3, 최소공배수는 12이므로 solution(3, 12)는 [3, 12]를 반환해야합니다.

# - 두 수는 1이상 1000000이하의 자연수입니다.

def solution(n,m):
    # 다른 사람 풀이를 보고 내가 만든 코드 ㅠㅠ
    answer = []
    for i in range(min(n,m)+1, 0, -1):
        if n % i == 0 and m % i == 0:
            answer.append(i)
            break
    for i in range(max(n,m),(n*m)+1):
        if i % n == 0 and i % m == 0:
            answer.append(i)
            break
    return answer
    # ==================================
    # 밑에 코드는 무식하게 한번 짜봤다.
    # 약수 전체를 만들고 전체를 비교해서 최대공약수를 찾았다.
    # 최소 공배수도 마찬가지로 배수를 n*m까지 만들고 그 중 2개의 리스트를 비교해서 최소 공배수를 찾았다.
    # 정확성 테스트에서는 떨어지진 않았지만 효율성 테스트에서 시간 초과가 나왔다...
    # answer = [0, 0]
    # # n의 약수 구하기
    # n_list = []
    # m_list = []
    # for i in range(1, n+1):
    #     if n % i == 0:
    #         n_list.append(i)
    # for i in range(1, m+1):
    #     if m % i == 0:
    #         m_list.append(i)
    # n_list.reverse()
    # m_list.reverse()
    # big_list = []
    # small_list = []
    # if len(n_list) > len(m_list):
    #     big_list = n_list
    #     small_list = m_list
    # elif len(n_list) < len(m_list):
    #     big_list = m_list
    #     small_list = n_list
    # else:
    #     big_list = n_list
    #     small_list = m_list
    # for i in range(0, len(big_list)):
    #     if answer[0] != 0:
    #         break
    #     for j in range(0, len(small_list)):
    #         if big_list[i] == small_list[j]:
    #             answer[0] = big_list[i]
    #             break
    # multiple = n * m
    # n_list = []
    # m_list = []
    # for i in range(1,multiple):
    #     n_list.append(n*i)
    #     m_list.append(m*i)
    # for i in range(0, len(n_list)):
    #     if answer[1] != 0:
    #         break
    #     for j in range(0, len(m_list)):
    #         if n_list[i] == m_list[j]:
    #             answer[1] = n_list[i]
    #             break
    # return answer

print(solution(3, 12))
print(solution(2, 5))