def solution(slice, n):
    for i in range(1,101,1) :
        if((i*slice)>=n) : break
    answer = i
    return answer