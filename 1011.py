# https://programmers.co.kr/learn/courses/30/lessons/12949
# 행렬의 곱셈

# <문제 설명>
# - 2차원 행렬 arr1과 arr2를 입력받아, arr1에 arr2를 곱한 결과를 반환하는 함수, solution을 완성해주세요.

# <제한 조건>
# - 행렬 arr1, arr2의 행과 열의 길이는 2 이상 100 이하입니다.
# - 행렬 arr1, arr2의 원소는 -10 이상 20 이하인 자연수입니다.
# - 곱할 수 있는 배열만 주어집니다.

# 행 - column
# 렬 - row
def solution(arr1, arr2):
    # 곱한 결과가 저장될 answer 리스트 생성
    answer = [[0 for j in range(len(arr2[0]))] for i in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr2)):
                answer[i][j] += arr1[i][k] * arr2[k][j]
    return answer

arr1 = [[1,2], [3,4]]
arr2 = [[1,2], [3,4]]
print(solution(arr1,arr2))

arr1 = [[1, 4], [3, 2], [4, 1]]
arr2 = [[3, 3], [3, 3]]
print(solution(arr1,arr2))

arr1 = [[2, 3, 2], [4, 2, 4], [3, 1, 4]]
arr2 = [[5, 4, 3], [2, 4, 1], [3, 1, 1]]
print(solution(arr1,arr2))