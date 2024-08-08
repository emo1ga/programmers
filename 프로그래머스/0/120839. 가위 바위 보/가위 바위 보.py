def solution(rsp):
    win = {
        '2' : '0',
        '0' : '5',
        '5' : '2'
    }
    answer = ''
    for move in rsp:
        answer += win[move]
    return answer