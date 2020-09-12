# https://programmers.co.kr/learn/courses/30/lessons/12930
# 이상한 문자 만들기

# <문제 설명>
# - 문자열 s는 한 개 이상의 단어로 구성되어 있습니다.
# - 각 단어는 하나 이상의 공백 문자로 구분되어 있습니다.
# - 각 단어의 짝수번째 알파벳은 대문자로, 홀수번째 알파벳은 소문자로 바꾼 문자열을 리턴하는 함수, solution을 완성하세요.

# <제한 사항>
# - 문자열 전체의 짝/홀수 인덱스가 아니라, 단어(공백을 기준)별로 짝/홀수 인덱스를 판단해야합니다.
# - 첫번째 글자는 0번재 인덱스로 보아 짝수번째 알파벳으로 처리해야 합니다.

def solution(s):
    # 내가 푼 문제 풀이
    # answer = ''
    # for i in s.split(' '):
    #     tmp = ''
    #     for j in range(0, len(i)):
    #         if j % 2 == 0:
    #             tmp += i[j].upper()
    #         else:
    #             tmp += i[j].lower()
    #     answer = answer + tmp + ' '
    # return answer[:-1]

    # 다른 사람 문제 풀이 참고해서 내가 만든 코드
    # 위의 코드와의 차이점은 enumerate 함수를 사용했다는 것
    # tmp 변수도 사용하지 않았다. - 최대한 메모리 절약 ㅋㅋㅋ 별 차이는 없지만 그래도 정신 승리!
    answer = ''
    for word in s.split(' '):
        for index, c in enumerate(word):
            if index % 2 == 0:
                answer += c.upper()
            else:
                answer += c.lower()
        answer += ' '
    return answer[:-1]
    
print(solution("try hello world"))
