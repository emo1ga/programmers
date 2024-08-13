def solution(n):
    answer = 0
    for i in range (1,n+1) :
        facj = 1
        for j in range (1, i+1) :
            facj*=j
            if(facj>n) :
                break
        if(facj<=n) :
            answer = i
    return answer