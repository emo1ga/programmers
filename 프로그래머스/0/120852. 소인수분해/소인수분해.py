def solution(n):
    answer = []
    for i in range (2,n+1) :
        a = 0
        for j in range (2, i+1) :
            if(i%j==0) :
                a += 1
        if(a==1) :
            if(n%i==0) :
                answer.append(i)
    return answer