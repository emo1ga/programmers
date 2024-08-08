def solution(balls, share):
    balls_all = 1
    for i in range (0, share) :
        balls_all *= balls-i
    share_all = 1
    for i in range (1, share+1) :
        share_all *= i
        
    answer = balls_all/share_all
    return answer