# https://codility.com/c/run/demoRFZ3A4-ABF

# 66 https://codility.com/demo/results/demoRFZ3A4-ABF/
# 100 https://codility.com/demo/results/demoNKB3GA-VXZ/

def solution(initial, final, step):
    diff = final - initial
    if diff % step == 0:
        return diff / step
    else:
        return (diff / step) + 1

test_data = [   
                (10, 85, 30, 3),
                (0, 12, 4, 3),
                (5, 5, 8, 0)
            ]

for d in test_data:
    print 'Testing [%d, %d, %d]' % (d[0], d[1], d[2])
    result = solution(d[0], d[1], d[2])
    if result == d[3]:
        print 'PASSED!'
    else:
        print 'FAILED!  Expected %d, got %d' % (d[3], result)