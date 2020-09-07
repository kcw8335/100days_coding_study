# https://programmers.co.kr/learn/courses/30/lessons/12935
# 제일 작은 수 제거하기

# <문제 설명>
# - 정수를 저장한 배열, arr에서 가장 작은 수를 제거한 배열을 리턴하는 함수, solution을 완성해주세요.
# - 단, 리턴하는 배열이 빈 배열인 경우엔 배열에 -1을 채워 리턴하세요.
# - 예를 들어 arr이 [4,3,2,1]인 경우는 [4,3,2]를 리턴하고 [10]면 [-1]을 리턴합니다.

# <제한 조건>
# - arr은 길이 1 이상인 배열이다.
# - 인덱스 i,j에 대해 i != j이면 arr[i] != arr[j] 입니다.


# 나도 드디어 2줄 코딩 성공했다... 한줄 코딩 하고 싶은데.. 아직인가 보다...
def solution(arr):
    # min 함수를 사용해서 arr의 최소값을 찾아낸 후
    # remove 함수를 사용해서 원소를 삭제했다.
    arr.remove(min(arr))
    # arr의 리스트의 원소 개수가 0개이면 [-1]리턴 아니면 arr를 그대로 리턴했다.
    return [-1] if len(arr) == 0 else arr

arr = [4,3,2,1]
print(solution(arr))
arr = [10]
print(solution(arr))