def solution(hp):
    Aants = hp // 5
    hp %= 5
    Bants = hp // 3
    hp %= 3
    Cants = hp // 1
    
    return Aants+Bants+Cants