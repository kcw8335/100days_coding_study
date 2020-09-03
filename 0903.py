# https://programmers.co.kr/learn/courses/30/lessons/12944
# 평균 구하기

# <문제 설명>
# - 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.

# <제한 사항>
# - arr은 길이 1 이상, 100 이하인 배열입니다.
# - arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
from functools import reduce
def solution(arr):
    # 내 문제 풀이
    # answer = 0
    # for i in arr:
    #     answer += i
    # answer /= len(arr)
    # return answer
    
    # 다른 사람 문제 풀이 ㅠㅠ
    # list에 sum함수를 사용할 수 있다는 걸 처음 알았다...
    # return (sum(arr) / len(arr))
    
    # reduce함수는 앞으로 유용하게 사용할 것 같다... 처음 알았다... 대박...
    # reduce(function, iterable, initializer=None)
    # reduce 함수는 iterable의 요소들을 function에 대입하여 결국 하나의 결과값을 리턴해주는 함수이다.
    # ex) ((((1+2)+3)+4)+5)
    return reduce(lambda x, y : x + y, arr) / len(arr)

arr = [1,2,3,4]
print(solution(arr))

arr = [5,5]
print(solution(arr))