def solution(sides):
    answer = 2
    if (max(sides)<(sum(sides)-max(sides))) :
        answer = 1
    return answer