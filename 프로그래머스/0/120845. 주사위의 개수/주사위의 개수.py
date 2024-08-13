def solution(box, n):
    for i in range (0,3) :
        box[i] //= n
    answer = box[0]*box[1]*box[2]
    return answer