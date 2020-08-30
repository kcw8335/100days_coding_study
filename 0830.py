# https://programmers.co.kr/learn/courses/30/lessons/12950
# 행렬의 덧셈

# <문제 설명>
# - 행렬의 덧셈은 행과 열의 크기가 같은 두 행렬의 같은 행, 같은 열의 값을 서로 더한 결과가 됩니다.
# - 2개의 행렬 arr1과 arr2를 입력받아, 행렬의 덧셈의 결과를 반환하는 함수, solution을 완성하세요.

# <제한 조건>
# - 행렬 arr1, arr2의 행과 열의 길이는 500을 넘지 않습니다.

def solution(arr1, arr2):
    answer = [[]]
    del answer[0]
    # 행 구하기
    column = len(arr1)
    # 렬 구하기
    row = len(arr1[0])
    # 이중 for문을 사용하여 행렬 원소에 접근
    for i in range(0, column):
        # arr1과 arr2의 각 행의 더한 값을 잠시 저장할 tmp 변수
        # 각 열의 연산이 끝나면 초기화해주는 기능도 있음
        tmp = []
        for j in range(0, row):
            # arr1, arr2 각 열의 값을 더해서 tmp 리스트 마지막에 원소 추가
            tmp.append(arr1[i][j] + arr2[i][j])
        # arr1, arr2의 각 행의 더한 값을 결과값에 추가
        answer.append(tmp)
    return answer

arr1 = [[1,2],[2,3]]
arr2 = [[3,4],[5,6]]
print(solution(arr1, arr2))
# 결과값 = [[4,6],[7,9]]

arr1 = [[1],[2]]
arr2 = [[3],[4]]
print(solution(arr1, arr2))
# 결과값 = [[4],[6]]