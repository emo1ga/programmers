def solution(n):
    for i in range (1, 101 ,1) :
        if((6*i)%n==0) : break
    answer = i
    return answer