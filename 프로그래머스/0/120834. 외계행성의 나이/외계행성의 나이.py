def solution(age):
    age_str = str(age)
    answer = ''.join(chr(97 + int(char)) for char in age_str)
    return answer