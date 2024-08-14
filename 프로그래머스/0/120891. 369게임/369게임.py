def solution(order):
    answer = 0
    for i in range (0,7) :
        if((order // (10**i) % 10)!=0) :
            if ((order//(10**i)%10)%3==0) :
                answer+=1
                if(order<10**(i+1)) : break
    return answer