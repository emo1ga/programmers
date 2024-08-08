def solution(numbers, direction):
    if(direction=="left") :
        numbers.append(numbers[0])
        numbers.pop(0)
    else :
        numbers.insert(0,numbers[-1])
        numbers.pop(-1)
    answer = numbers
    return answer