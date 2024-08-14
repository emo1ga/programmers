def solution(array, n):
    array.sort()
    answer = array[0]
    for i in range(1, len(array)):
        if abs(n - array[i]) < abs(n - answer):
            answer = array[i]
    return answer