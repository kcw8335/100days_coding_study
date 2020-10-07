# https://programmers.co.kr/learn/courses/30/lessons/17682
# 다트 게임

# <문제설명>
# - 카카오톡에 뜬 네 번째 별! 심심할 땐? 카카오톡 게임별~

# - 카카오톡 게임별의 하반기 신규 서비스로 다트 게임을 출시하기로 했다.
# - 다트 게임은 다트판에 다트를 세 차례 던져 그 점수의 합계로 실력을 겨루는 게임으로, 모두가 간단히 즐길 수 있다.

# - 갓 입사한 무지는 코딩 실력을 인정받아 게임의 핵심 부분인 점수 계산 로직을 맡게 되었다.
# - 다트 게임의 점수 계산 로직은 아래와 같다.

# - 1. 다트 게임은 총 3번의 기회로 구성된다.
# - 2. 각 기회마다 얻을 수 있는 점수는 0점에서 10점까지이다.
# - 3. 점수와 함께 Single(S), Double(D), Triple(T) 영역이 존재하고 각 영역 당첨 시 점수에서 1제곱, 2제곱, 3제곱 (점수1 , 점수2 , 점수3 )으로 계산된다.
# - 4. 옵션으로 스타상(*) , 아차상(#)이 존재하며 스타상(*) 당첨 시 해당 점수와 바로 전에 얻은 점수를 각 2배로 만든다. 아차상(#) 당첨 시 해당 점수는 마이너스된다.
# - 5. 스타상(*)은 첫 번째 기회에서도 나올 수 있다. 이 경우 첫 번째 스타상(*)의 점수만 2배가 된다. (예제 4번 참고)
# - 6. 스타상(*)의 효과는 다른 스타상(*)의 효과와 중첩될 수 있다. 이 경우 중첩된 스타상(*) 점수는 4배가 된다. (예제 4번 참고)
# - 7. 스타상(*)의 효과는 아차상(#)의 효과와 중첩될 수 있다. 이 경우 중첩된 아차상(#)의 점수는 -2배가 된다. (예제 5번 참고)
# - 8. Single(S), Double(D), Triple(T)은 점수마다 하나씩 존재한다.
# - 9. 스타상(*), 아차상(#)은 점수마다 둘 중 하나만 존재할 수 있으며, 존재하지 않을 수도 있다.

# - 0~10의 정수와 문자 S, D, T, *, #로 구성된 문자열이 입력될 시 총점수를 반환하는 함수를 작성하라.

# <입력 형식>
# - 점수|보너스|[옵션]으로 이루어진 문자열 3세트.
# - 예) 1S2D*3T
#   - 점수는 0에서 10 사이의 정수이다.
#   - 보너스는 S, D, T 중 하나이다.
#   - 옵선은 *이나 # 중 하나이며, 없을 수도 있다.

# <출력 형식>
# - 3번의 기회에서 얻은 점수 합계에 해당하는 정수값을 출력한다.
# - 예) 37

# def solution(dartResult):
#     answer = 0
#     tmp_dict1 = {
#         "S":1,
#         "D":2,
#         "T":3
#     }
#     tmp_dict2 = {
#         "*":2,
#         "#":-1
#     }
#     tmp_num = 0
#     tmp_num1 = 0
#     tmp_num2 = 0
#     tmp_num3 = 0
#     index = 1
#     for i in range(len(dartResult)):
#         # 숫자 1이라면... 10을 또 고려해야함
#         if dartResult[i] == "1":
#             # 숫자 10이라면
#             if dartResult[i+1] == "0":
#                 tmp_num = 10
#                 i += 1
#                 continue
#             # 숫자 1이 확정이라면
#             else:
#                 tmp_num = 1
#         # 숫자 2,3,4,5,6,7,8,9 중 한 개라면
#         elif dartResult[i] in ["2","3","4","5","6","7","8","9"]:
#             tmp_num = int(dartResult[i])

#         # S, D, T 중 한 개라면
#         elif dartResult[i] in tmp_dict1.keys():
#             if index == 1:
#                 tmp_num1 = tmp_num ** tmp_dict1[dartResult[i]]
#             elif index == 2:
#                 tmp_num2 = tmp_num ** tmp_dict1[dartResult[i]]
#             elif index == 3:
#                 tmp_num3 = tmp_num ** tmp_dict1[dartResult[i]]
#             tmp_num = 0
#             try:
#                 if dartResult[i+1] not in tmp_dict2.keys():
#                     index += 1
#             except:
#                 break
#         # *, # 중 한 개라면        
#         elif dartResult[i] in tmp_dict2.keys():
#             if dartResult[i] == "*":
#                 if index == 1:
#                     tmp_num1 *= tmp_dict2[dartResult[i]]
#                 elif index == 2:
#                     tmp_num1 *= tmp_dict2[dartResult[i]]
#                     tmp_num2 *= tmp_dict2[dartResult[i]]
#                 elif index == 3:
#                     tmp_num2 *= tmp_dict2[dartResult[i]]
#                     tmp_num3 *= tmp_dict2[dartResult[i]]
#                 index += 1
#             elif dartResult[i] == "#":
#                 if index == 1:
#                     tmp_num1 *= tmp_dict2[dartResult[i]]
#                 elif index == 2:
#                     tmp_num2 *= tmp_dict2[dartResult[i]]
#                 elif index == 3:
#                     tmp_num3 *= tmp_dict2[dartResult[i]]
#                 index += 1
#     answer = tmp_num1 + tmp_num2 + tmp_num3
#     return answer

# 다른 사람 문제 풀이
# ... 정규 표현식을 사용해서 풀었다고 한다... 대단하다...
import re

def solution(dartResult):
    bonus = {'S' : 1, 'D' : 2, 'T' : 3}
    option = {'' : 1, '*' : 2, '#' : -1}
    p = re.compile('(\d+)([SDT])([*#]?)')
    dart = p.findall(dartResult)
    print(dart)
    for i in range(len(dart)):
        if dart[i][2] == '*' and i > 0:
            dart[i-1] *= 2
        dart[i] = int(dart[i][0]) ** bonus[dart[i][1]] * option[dart[i][2]]

    answer = sum(dart)
    return answer

dartResult = "1S2D*3T"
print(solution(dartResult))

# dartResult = "1D2S#10S"
# print(solution(dartResult))

# dartResult = "1D2S0T"
# print(solution(dartResult))

# dartResult = "1S*2T*3S"
# print(solution(dartResult))

# dartResult = "1D#2S*3S"
# print(solution(dartResult))

# dartResult = "1T2D3D#"
# print(solution(dartResult))

# dartResult = "1D2S3T*"
# print(solution(dartResult))