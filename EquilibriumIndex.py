import sys
from random import choice

def solution(numbers):
    left_sum = 0
    total_sum = sum(numbers)
    for i, k in enumerate(numbers):
        right_sum = total_sum - k
        if left_sum == right_sum:
            return i
        left_sum += k
        total_sum -= k
    return -1

input = [-7, 1, 5, 2, -4, 3, 0]
print solution(input)
sys.exit(1)

def num(foo):
    return choice(range(-foo, foo))

N = 100
input = [num(N) for x in range(N)]
print solution(input)
