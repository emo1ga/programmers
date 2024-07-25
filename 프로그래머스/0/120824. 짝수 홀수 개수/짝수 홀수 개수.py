def solution(num_list):
    z = 0
    for i in range (0, len(num_list)) :
        if (num_list[i] % 2 == 0) :
            z += 1
    h = len(num_list)-z
    answer = [z,h]
    return answer