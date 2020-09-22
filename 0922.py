# https://programmers.co.kr/learn/courses/30/lessons/12916
# 문자열 내 p와 y의 개수

# <문제 설명>
# - 대문자와 소문자가 섞여있는 문자열 s가 주어집니다. 
# - s에 'p'의 개수와 'y'의 개수를 비교해 같으면 True, 다르면 False를 return 하는 solution를 완성하세요. 
# - 'p', 'y' 모두 하나도 없는 경우는 항상 True를 리턴합니다.
# - 단, 개수를 비교할 때 대문자와 소문자는 구별하지 않습니다.
# - 예를 들어 s가 pPoooyY면 true를 return하고 Pyy라면 false를 return합니다.

# <제한 사항>
# - 문자열 s의 길이 : 50 이하의 자연수
# - 문자열 s는 알파벳으로만 이루어져 있습니다.

def solution(s):
    how_many_p = 0
    how_many_y = 0
    # p와 y의 개수를 반복문을 사용해서 변수 how_many_p와 how_many_y에 저장했다.
    for i in range(len(s)):
        if s[i] == "p" or s[i] == "P":
            how_many_p += 1
        elif s[i] == "y" or s[i] == "Y":
            how_many_y += 1
    # p의 개수와 y의 개수가 같으면 Ture 다르면 False
    if how_many_y == how_many_p:
        return True
    else:
        return False

    # 다른 사람 문제 풀이 - ㅠㅠ 전부 소문자로 바꾸고 count 함수만 사용해서 끝냈다. count함수를 처음 알았다...

    return s.lower().count('p') == s.lower().count('y')

print(solution("pPoooyY"))
print(solution("Pyy"))