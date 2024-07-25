def solution(array):
    # 빈도 계산을 위한 딕셔너리 생성
    frequency = {}
    
    # 배열의 각 요소에 대해 빈도 계산
    for num in array:
        if num in frequency:
            frequency[num] += 1
        else:
            frequency[num] = 1
    
    # 최빈값과 그 빈도를 초기화
    max_count = 0
    mode = -1
    multiple_modes = False
    
    # 딕셔너리를 순회하며 최빈값을 찾음
    for num, count in frequency.items():
        if count > max_count:
            max_count = count
            mode = num
            multiple_modes = False
        elif count == max_count:
            multiple_modes = True
    
    # 최빈값이 여러 개인 경우 -1 반환
    if multiple_modes:
        return -1
    else:
        return mode