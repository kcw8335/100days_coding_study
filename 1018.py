# https://programmers.co.kr/learn/courses/30/lessons/12909
# 올바른 괄호

# <문제 설명>
# - 괄호가 바르게 짝지어졌다는 것은 '(' 문자로 열렸으면 반드시 짝지어서 ')' 문자로 닫혀야 한다는 뜻입니다.
# - 예를 들어
#   - ()() 또는 (())() 는 올바른 괄호입니다.
#   - )()( 또는 (()( 는 올바르지 않은 괄호입니다.

# - '(' 또는 ')' 로만 이루어진 문자열 s가 주어졌을 때,
# - 문자열 s가 올바른 괄호이면 true를 return 하고,
# - 올바르지 않은 괄호이면 false를 return 하는 solution 함수를 완성해 주세요.

# <제한 사항>
# - 문자열 s의 길이 : 100,000 이하의 자연수
# - 문자열 s는 '(' 또는 ')' 로만 이루어져 있습니다.

# stack을 활용하여 문제풀었다... 힘들었다...
# pop, del, remove 함수의 활용을 잘하자!!!
def solution(s):
    # s의 개수가 홀수이면 당연히 False
    # 맨앞글자가 ")"이면 False 맨뒷글자가 "("이면 False
    if s[0] == ")" or s[len(s)-1] == "(" or len(s) % 2 == 1:
        return False
    
    tmp_list = []
    for i in s:
        if i == "(":
            tmp_list.append(i)
        elif i == ")":
            try:
                tmp_list.pop()
            except:
                return False
    if len(tmp_list) == 0:
        return True
    else:
        return False
    
s = "()))((()"
print(solution(s))

s = "())())"
print(solution(s))

s = "()()"
print(solution(s))

s = "(())()"
print(solution(s))

s = ")()("
print(solution(s))

s = "(()("
print(solution(s))