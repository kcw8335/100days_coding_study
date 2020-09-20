# https://programmers.co.kr/learn/courses/30/lessons/12918
# 문자열 다루기 기본

# <문제 설명>
# - 문자열 s의 길이가 4 혹은 6이고, 숫자로만 구성돼있는지 확인해주는 함수, solution을 완성하세요.
# - 예를 들어 s가 a234이면 False를 리턴하고 1234라면 True를 리턴하면 됩니다.

# <제한 사항>
# - s는 길이 1 이상, 길이 8 이하인 문자열입니다.

def solution(s):
    if len(s) != 4 and len(s) != 6:
        return False
    try:
        int(s)
        return True
    except:
        return False

    # 다른 사람 문제 풀이 - ㅠㅠ 이렇게 간단하게 끝나는 문제를 나는...
    return s.isdigit() and len(s) in (4,6)


s = "a234"
print(solution(s))
s = "1234"
print(solution(s))

s = "a"
print(solution(s))