# https://codility.com/c/run/demoCDNNWT-9T9

# 0 in 8min https://codility.com/demo/results/demoCDNNWT-9T9/
# 18 in 5min https://codility.com/demo/results/demoMT8HNE-8MX/
# 72 in 7min https://codility.com/demo/results/demo2WS7VA-AJV/
# 100 in 4min https://codility.com/demo/results/demoA6N8PY-4KQ/

import random
import sys

def solution(X, A):
    print 'Solving for %d and %s...' % (X, A)
    river = [0] * (X + 1)
    leaf_count = 0
    for i, a in enumerate(A):
        if a <= X and not river[a]:
            river[a] = 1
            leaf_count += 1
            print river, leaf_count
            if leaf_count == X:
                return i
    return -1


N = 10
inp = range(1, N)
random.shuffle(inp)
print solution(N - 1, inp)
print solution(5, [1, 3, 1, 4, 2, 3, 5, 4])
print solution(5, [1, 3, 1, 4, 2, 3, 3, 4])
