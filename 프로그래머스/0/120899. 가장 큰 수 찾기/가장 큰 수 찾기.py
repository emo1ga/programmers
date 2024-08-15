def solution(array):
    answer = []
    a = array.copy()
    array.sort()
    b = array[len(array)-1]
    c = a.index(b)
    answer.append(b)
    answer.append(c)
    return answer