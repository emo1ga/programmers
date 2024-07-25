def solution(money):
    cup = money//5500
    mon = money-(5500*cup)
    answer = [cup,mon]
    return answer