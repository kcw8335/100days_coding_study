# https://programmers.co.kr/learn/courses/30/lessons/12903
# 가운데 글자 가져오기

# <문제 설명>
# - 단어 s의 가운데 글자를 반환하는 함수, solution을 만들어 보세요.
# - 단어의 길이가 짝수라면 가운데 두글자를 반환하면 됩니다.

# <재한 사항>
# - s는 길이가 1 이상, 100이하인 스트링입니다.

def solution(s):
    # 꾸역꾸역 한줄로 작성해보았다.ㅠㅠ 효율성 없는 거 같긴한데... 잘 모르겠다...
    return s[(len(s) // 2)] if len(s) % 2 == 1 else s[(len(s) // 2) - 1] + s[(len(s) // 2)] 


print(solution("abcde"))
print(solution("qwer"))