# https://programmers.co.kr/learn/courses/30/lessons/12906
# 같은 숫자는 싫어

# <문제 설명>
# - 배열 arr가 주어집니다.
# - 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어져 있습니다.
# - 이때, 배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 합니다.
# - 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야 합니다.
# - 예를 들면, arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1] 을 return 합니다.
# - arr = [4, 4, 4, 3, 3] 이면 [4, 3] 을 return 합니다.
# - 배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성해 주세요.

# <제한사항>
# - 배열 arr의 크기 : 1,000,000 이하의 자연수
# - 배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수

def solution(arr):
    # 정확성 테스트는 통과했지만 효율성 테스트를 통과하지 못했다...
    # 반복문을 두번 돌려서 그런가하고 수정을 시도했다...
    # tmp = list()
    # answer = list()
    # for i in range(len(arr)-1):
    #     if arr[i] == arr[i+1]:
    #         tmp.append(i)
    # for i in range(len(arr)):
    #     if i not in tmp:
    #         answer.append(arr[i])
    # return answer

    # 반복문을 한번만 돌렸지만 그래도 효율성 테스트를 통과하지 못했다...
    # 아마 문제는 01 12 23 이렇게 비교해서 효율성면에서 안좋았나 보다...
    # try:
    #     i = 0
    #     while(True):
    #         if arr[i] == arr[i+1]:
    #             del arr[i]
    #         else:
    #             i+=1
    # except:
    #     pass
    # return arr

    # 결국 구글링을 한 결과...
    # 답은 쉽게 나왔다... 
    # 마지막 수와 tmp리스트에 i번째 값이 다르면 i를 추가하면 되더라...
    tmp = [arr[0]]
    for i in range(1, len(arr)):
        if tmp[-1] != arr[i]:
            tmp.append(arr[i])
    return tmp

print(solution([1,1,3,3,0,1,1]))
print(solution([4,4,4,3,3]))