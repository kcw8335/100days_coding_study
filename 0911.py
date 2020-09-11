# https://programmers.co.kr/learn/courses/30/lessons/12931?language=python3
# 자릿수 더하기

# <문제 설명>
# - 자연수 N이 주어지면, N의 각 자릿수의 합을 구해서 return 하는 solution 함수를 만들어 주세요.
# - 예를 들어 N = 123이면 1 + 2 + 3 = 6을 return 하면 됩니다.

# <제한사항>
# - N의 범위 : 100,000,000 이하의 자연수

# 드디어 한줄 코딩 성공 ㅎㅎㅎ
def solution(n):
    # 자연수 n을 문자형 리스트로 바꾸고
    # map 함수를 이용해서 int형 리스트로 바꾸고
    # sum 함수를 사용해서 int형 리스트의 값들을 전부 더했다.
    return sum(list(map(int, list(str(n)))))

    # 다른 사람 문제 풀이
    # int형 리스트로 바꿀 필요없이 map함수의 리턴값을 sum함수로 사용해도 된다...
    # 어쩐지 실행시간이 길더라...
    return sum(map(int, list(str(n))))
    

print(solution(123))
print(solution(987))