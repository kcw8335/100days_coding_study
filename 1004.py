# https://programmers.co.kr/learn/courses/30/lessons/67256
# [카카오 인턴] 키패드 누르기

# <문제 설명>
# - 스마트폰 전화 키패드의 각 칸에 다음과 같이 숫자들이 적혀 있습니다.
# - 이 전화 키패드에서 왼손과 오른손의 엄지손가락만을 이용해서 숫자만을 입력하려고 합니다.
# - 맨 처음 왼손 엄지손가락은 * 키패드에 오른손 엄지손가락은 # 키패드 위치에서 시작하며, 엄지손가락을 사용하는 규칙은 다음과 같습니다.

# - 1. 엄지손가락은 상하좌우 4가지 방향으로만 이동할 수 있으며 키패드 이동 한 칸은 거리로 1에 해당합니다.
# - 2. 왼쪽 열의 3개의 숫자 1, 4, 7을 입력할 때는 왼손 엄지손가락을 사용합니다.
# - 3. 오른쪽 열의 3개의 숫자 3, 6, 9를 입력할 때는 오른손 엄지손가락을 사용합니다.
# - 4. 가운데 열의 4개의 숫자 2, 5, 8, 0을 입력할 때는 두 엄지손가락의 현재 키패드의 위치에서 더 가까운 엄지손가락을 사용합니다.
# - 4-1. 만약 두 엄지손가락의 거리가 같다면, 오른손잡이는 오른손 엄지손가락, 왼손잡이는 왼손 엄지손가락을 사용합니다.

# - 순서대로 누를 번호가 담긴 배열 numbers, 
# - 왼손잡이인지 오른손잡이인 지를 나타내는 문자열 hand가 매개변수로 주어질 때, 
# - 각 번호를 누른 엄지손가락이 왼손인 지 오른손인 지를 나타내는 연속된 문자열 형태로 return 하도록 solution 함수를 완성해주세요.

# <제한 사항>
# - numbers 배열의 크기는 1 이상 1,000 이하입니다.
# - numbers 배열 원소의 값은 0 이상 9 이하인 정수입니다.
# - hand는 "left" 또는 "right" 입니다.
# - "left"는 왼손잡이, "right"는 오른손잡이를 의미합니다.
# - 왼손 엄지손가락을 사용한 경우는 L, 오른손 엄지손가락을 사용한 경우는 R을 순서대로 이어붙여 문자열 형태로 return 해주세요.
# 거리구하는 함수(눌러야할 번호, 손의 위치)
def distance(number, hand_location):
    if number == hand_location:
        return 0
    if number == 2:
        if hand_location in [1,3,5]:
            return 1
        elif hand_location in [4,6,8]:
            return 2
        elif hand_location in [7,9,0]:
            return 3
        elif hand_location in ["*","#"]:
            return 4
    elif number == 5:
        if hand_location in [2,4,6,8]:
            return 1
        elif hand_location in [1,3,7,9,0]:
            return 2
        elif hand_location in ["*","#"]:
            return 3
    elif number == 8:
        if hand_location in [5,7,9,0]:
            return 1
        elif hand_location in [2,4,6,"*","#"]:
            return 2
        elif hand_location in [1,3]:
            return 3
    elif number == 0:
        if hand_location in [8,"*","#"]:
            return 1
        elif hand_location in [5,7,9]:
            return 2
        elif hand_location in [2,4,6]:
            return 3
        elif hand_location in [1,3]:
            return 4

def solution(numbers, hand):
    answer = ''
    # 초기 손 위치 설정
    left_hand_loction = "*"
    right_hand_loction = "#"
    for i in numbers:
        # 1 4 7 을 누를 때는 무조건 왼손 사용
        if i in [1,4,7]:
            answer += "L"
            left_hand_loction = i
        # 3 6 9 를 누를 때는 무조건 오른손 사용
        elif i in [3,6,9]:
            answer += "R"
            right_hand_loction = i
        # 2 5 8 0 중 하나를 누를 때 어떤 손을 사용해야 하는 지??
        elif i in [2,5,8,0]:
            # 눌러야 할 번호와 왼손의 위치와의 거리
            distance_from_number_to_left_hand_location = distance(i, left_hand_loction)
            # 눌러야 할 번호와 오른손의 위치와의 거리
            distance_from_number_to_right_hand_location = distance(i, right_hand_loction)
            # 왼손의 거리와 오른손의 거리가 같다면 
            if distance_from_number_to_left_hand_location == distance_from_number_to_right_hand_location:
                if hand == "left":
                    answer += "L"
                    left_hand_loction = i
                elif hand == "right":
                    answer += "R"
                    right_hand_loction = i
            elif distance_from_number_to_left_hand_location > distance_from_number_to_right_hand_location:
                answer += "R"
                right_hand_loction = i
            elif distance_from_number_to_left_hand_location < distance_from_number_to_right_hand_location:
                answer += "L"
                left_hand_loction = i
    return answer

numbers = [1,3,4,5,8,2,1,4,5,9,5]
hand = "right"
print(solution(numbers, hand))

numbers = [7,0,8,2,8,3,1,5,7,6,2]
hand = "left"
print(solution(numbers, hand))

numbers = [1,2,3,4,5,6,7,8,9,0]
hand = "right"
print(solution(numbers, hand))