# https://programmers.co.kr/learn/courses/30/lessons/12951
# JadenCase 문자열 만들기

# <문제 설명>
# - JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
# - 문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

# <제한 조건>
# - s는 길이 1 이상인 문자열입니다.
# - s는 알파벳과 공백문자(" ")로 이루어져 있습니다.
# - 첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )
# def specific_index_replacement(string, index):
#     tmp_list = list(string)
#     tmp_list[index] = tmp_list[index].upper()
#     string = "".join(tmp_list)
#     return string

# def solution(s):
#     s = s.lower()
#     for i in range(len(s)):
#         # 첫번째 문자가 숫자이면 continue, 문자라면 대문자로 변경
#         if i == 0:
#             if s[i] in ["1","2","3","4","5","6","7","8","9"]:
#                 continue
#             if s[0] not in ["1","2","3","4","5","6","7","8","9"]:
#                 s = specific_index_replacement(s,i)
#         # 마지막 문자가 공백이라면 continue
#         elif s[i] == " " and len(s) == i:
#             continue
#         # 중간에 공백 문자들 다음에 오는 문자가 
#         elif s[i] == " ":
#             if s[i+1] == " ":
#                 continue
#             else:
#                 s = specific_index_replacement(s,i+1)
#     return s

# 위의 코드로 실행한 결과 런타임 에러가 나왔다...
# split 함수에 " " 공백을 넣으면 되는 데... 공백을 안 넣으면 에러난다... - 자세한 이유 생략
# def solution(s):
#     tmp_list = s.split(" ")
#     for i in range(len(tmp_list)):
#         tmp_list[i] = tmp_list[i].capitalize()
#     answer = " ".join(tmp_list)
#     return answer

# 다른 사람 문제 풀이...
# 내장함수가 있었다... 이걸 몰랐다...
def solution(s):
    return s.title()

s = "3people unFollowed me"
print(solution(s))

s = "for the last week"
print(solution(s))
