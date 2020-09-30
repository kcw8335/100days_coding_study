# https://programmers.co.kr/learn/courses/30/lessons/42840?language=python3
# 모의고사

# <문제 설명>
# - 수포자는 수학을 포기한 사람의 준말입니다.
# - 수포자 삼인방은 모의고사에 수학 문제를 전부 찍으려 합니다.
# - 수포자는 1번 문제부터 마지막 문제까지 다음과 같이 찍습니다.

# - 1번 수포자가 찍는 방식: 1, 2, 3, 4, 5, 1, 2, 3, 4, 5, ...
# - 2번 수포자가 찍는 방식: 2, 1, 2, 3, 2, 4, 2, 5, 2, 1, 2, 3, 2, 4, 2, 5, ...
# - 3번 수포자가 찍는 방식: 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 3, 3, 1, 1, 2, 2, 4, 4, 5, 5, ...

# - 1번 문제부터 마지막 문제까지의 정답이 순서대로 들은 배열 answers가 주어졌을 때,
# - 가장 많은 문제를 맞힌 사람이 누구인지 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# <제한 조건>
# - 시험은 최대 10,000 문제로 구성되어있습니다.
# - 문제의 정답은 1, 2, 3, 4, 5중 하나입니다.
# - 가장 높은 점수를 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬해주세요.

# 이 함수는 학생들의 OMR카드를 작성하는 것과 같다고 생각하면 된다.
def make_stu_answer(answers, stu):
    if len(answers) > len(stu):
        stu = (stu * (len(answers)//len(stu))) + (stu[0:len(answers)%len(stu)])    
        return stu
    else:
        return stu[:len(answers)]

def solution(answers):
    answer = []
    stu_1 = [1,2,3,4,5]
    stu_2 = [2,1,2,3,2,4,2,5]
    stu_3 = [3,3,1,1,2,2,4,4,5,5]
    students = [stu_1, stu_2, stu_3]
    correct_answer = [0,0,0]
    
    # 학생이 3명이니깐 3번 반복한다.
    for i in range(len(students)):
        # 학생들의 OMR카드를 작성한다.
        students[i] = make_stu_answer(answers, students[i])
        # 문제 수 만큼 반복해서 몇 문제를 맞췄는지 검사한다.
        for j in range(len(answers)):
            if students[i][j] == answers[j]:
                correct_answer[i] += 1
    # 최대로 많이 맞춘 사람의 리스트를 만듭니다.
    # 만약 같다면 추가추가 ㅎㅎ
    for i in range(3):
        if correct_answer[i] == max(correct_answer):
            answer.append(i+1)
    return answer

# 그래도 이번에는 깔끔하게 성공한 것 같아 기분이 좋다 ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
print(solution([1,2,3,4,5]))
print(solution([1,3,2,4,2]))