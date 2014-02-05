# https://codility.com/c/run/demoKWTWXS-7KR

# 66 in 35min https://codility.com/demo/results/demoKWTWXS-7KR/
# 77 https://codility.com/demo/results/demo6HJC2G-WKH/
# 100 w SO help https://codility.com/demo/results/demoDR8XR9-GXD/

import random
import sys

def solution(N, A):
    counters = [0] * N
    m = 0
    min_value = 0
    for a in A:
        if a == N + 1:
            min_value = m
        else:
            counters[a - 1] = max(counters[a - 1], min_value) + 1
            if counters[a - 1] > m:
                m = counters[a - 1]
    for i in range(N):
        counters[i] = max(counters[i], min_value)
    return counters



N = 5
A = [3, 4, 4, 6, 1, 4, 4]
O = [3, 2, 2, 4, 2]

print '%s should be %s' % (solution(N, A), O)


MAX = 80
N = random.randint(1, MAX)
M = random.randint(1, MAX)
choices = [N + 1] * 10
A = [random.randint(1, N + 1) for _ in range(M)]

print '%s should be ...' % solution(N, A)


N = 8
A = [9, 9, 9, 9, 9, 9, 9]
O = [0, 0, 0, 0, 0, 0, 0, 0]

print '%s should be %s' % (solution(N, A), O)
