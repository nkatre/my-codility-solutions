# https://codility.com/c/run/demoRNNGK7-MK3

# 100 in 9min https://codility.com/demo/results/demoRNNGK7-MK3/
# (But I thought this would be O(nlog(n)) instead of the desired O(n)!
def solution(A):
    if sorted(A) == range(1, len(A) + 1):
        return 1
    else:
        return 0
