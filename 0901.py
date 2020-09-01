# https://programmers.co.kr/learn/courses/30/lessons/12948
# 핸드폰 번호 가리기

# <문제 설명>
# 프로그래머스 모바일은 개인정보 보호를 위해 고지서를 보낼 때 고객들의 전화번호의 일부를 가립니다.
# 전화번호가 문자열 phone_number로 주어졌을 때, 전화번호의 뒷 4자리를 제외한 나머지 숫자를 전부 *으로 가린 문자열을 리턴하는 함수, solution을 완성해주세요.

# <제한 조건>
# s는 길이 4 이상, 20이하인 문자열입니다.

def solution(phone_number):
    # 내가 푼 문제풀이 ㅠㅠ
    # <코드 설명>
    # 테이블 형식으로 변환할 문자를 인덱스 번호로 1대1 매칭
    table = str.maketrans('0123456789', '**********')
    # 뒤의 숫자 4자리만 남겨야 하므로 basis라는 기준을 만들었습니다.
    basis  = len(phone_number) - 4
    # 앞의 숫자는 *로 변환하고 뒤의 숫자를 더하기 연산으로 문자열 생성 후 리턴
    return phone_number[:basis].translate(table) + phone_number[basis:]

    # 다른 사람 문제풀이
    # return '*' * (len(phone_number)-4) + phone_number[-4:]

phone_number = '01033334444'
print(solution(phone_number))

phone_number = '027778888'
print(solution(phone_number))