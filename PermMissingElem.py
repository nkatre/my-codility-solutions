# https://codility.com/c/run/demoP7MYNC-U3S

# 100 in 15min https://codility.com/demo/results/demoP7MYNC-U3S/

def solution(A):
    total = sum(A)
    expected_total = sum(range(len(A) + 2))
    return expected_total - total

input = [2, 3, 4, 1]

print solution(input)