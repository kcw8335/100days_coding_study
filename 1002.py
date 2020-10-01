# https://programmers.co.kr/learn/courses/30/lessons/42576
# 완주하지 못한 선수

# <문제 설명>

# - 수많은 마라톤 선수들이 마라톤에 참여하였습니다.
# - 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.

# - 마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 
# - 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 
# - 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

# <제한 사항>
# - 마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
# - completion의 길이는 participant의 길이보다 1 작습니다.
# - 참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
# - 참가자 중에는 동명이인이 있을 수 있습니다.

def solution(participant, completion):
    completion.sort()
    participant.sort()
    for i in range(len(participant)):
        if completion[i] != participant[i]:
            return participant[i]

# 다른 사람 문제 풀이
# 객체 - 객체는 가능하다...
# 리스트 - 리스트는 불가능하니깐 이렇게 하네 ㅠㅠ 한 수 배웠다...
import collections

def solution(participant, completion):
    answer = collections.Counter(participant) - collections.Counter(completion)
    print(answer)
    print(answer.keys())
    return list(answer.keys())[0]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))

participant = ["marina", "josipa", "nikola", "vinko", "filipa"]
completion = ["josipa", "filipa", "marina", "nikola"]
print(solution(participant, completion))

participant = ["mislav", "stanko", "mislav", "ana"]
completion = ["stanko", "ana", "mislav"]
print(solution(participant, completion))