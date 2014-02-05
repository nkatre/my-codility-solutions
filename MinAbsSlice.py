def solution(A):
    m = min(A)
    # find minimum element m;
    m = min(abs(a) for a in A)
    print m



input = [[2, -4, 6, -3, 9]]

for i in input:
    print 'Running on', i
    print solution(i)
    print