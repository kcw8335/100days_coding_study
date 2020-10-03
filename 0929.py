# https://programmers.co.kr/learn/courses/30/lessons/42748
# K번째수

# <문제 설명>
# - 배열 array의 i번째 숫자부터 j번째 숫자까지 자르고 정렬했을 때, k번째에 있는 수를 구하려 합니다.
# - 예를 들어 array가 [1, 5, 2, 6, 3, 7, 4], i = 2, j = 5, k = 3이라면 array의 2번째부터 5번째까지 자르면 [5, 2, 6, 3]입니다.
# - 1에서 나온 배열을 정렬하면 [2, 3, 5, 6]입니다.
# - 2에서 나온 배열의 3번째 숫자는 5입니다.
# - 배열 array, [i, j, k]를 원소로 가진 2차원 배열 commands가 매개변수로 주어질 때,
# - commands의 모든 원소에 대해 앞서 설명한 연산을 적용했을 때 나온 결과를 배열에 담아 return 하도록 solution 함수를 작성해주세요.

# <제한 사항>
# - array의 길이는 1 이상 100 이하입니다.
# - array의 각 원소는 1 이상 100 이하입니다.
# - commands의 길이는 1 이상 50 이하입니다.
# - commands의 각 원소는 길이가 3입니다.

def solution(array, commands):
    # answer = []
    # for i in range(len(commands)):
    #     answer.append(sorted(array[(commands[i][0]-1) : commands[i][1]])[(commands[i][2]-1)])
    # return answer

    # 다른 사람 문제 풀이 - ㅠㅠ 어떻게 이런 생각을 하지ㅠㅠ 나도 람다에 대해 좀 더 관대해져야지...
    return list(map(lambda x:sorted(array[x[0]-1:x[1]])[x[2]-1], commands))

		
array = [1, 5, 2, 6, 3, 7, 4]
commands = [[2, 5, 3], [4, 4, 1], [1, 7, 3]]
print(solution(array, commands))
# 정답 - [5, 6, 3]