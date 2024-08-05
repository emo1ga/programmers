def solution(emergency):
    answer = []
    for i in range(len(emergency)):
        count = 1
        for j in range(len(emergency)):
            if emergency[j] > emergency[i]:
                count += 1
        answer.append(count)
    return answer