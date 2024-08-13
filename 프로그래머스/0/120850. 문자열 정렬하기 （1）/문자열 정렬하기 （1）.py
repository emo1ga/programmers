import re

def solution(my_string):
    numbers = [int(num) for num in my_string if num.isdigit()]
    numbers.sort()
    return numbers