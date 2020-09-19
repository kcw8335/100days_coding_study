# https://programmers.co.kr/learn/courses/30/lessons/12919
# 서울에서 김서방 찾기

# <문제 설명>
# - String형 배열 seoul의 element중 Kim의 위치 x를 찾아, 김서방은 x에 있다는 String을 반환하는 함수, solution을 완성하세요.
# - seoul에 Kim은 오직 한 번만 나타나며 잘못된 값이 입력되는 경우는 없습니다.

# <제한 사항>
# - seoul은 길이 1 이상, 1000 이하인 배열입니다.
# - seoul의 원소는 길이 1 이상, 20 이하인 문자열입니다.
# - Kim은 반드시 seoul 안에 포함되어 있습니다.

# 리스트 안의 값을 매개변수로 하는 index함수를 사용하여 김서방을 찾았다.
def solution(seoul):
    return "김서방은 " + str(seoul.index("Kim")) + "에 있다"


seoul = ["Jane", "Kim"]
print(solution(seoul))