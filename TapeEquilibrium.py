# https://codility.com/c/intro/demoEC7VNX-WEN
# Got a score of 91, because I used an initial min_diff of 1000 (expected 2000)
# Fixed it and got a score of 100.  Yay!
def solution(A):
    min_diff = 2000000000
    left_sum = A[0]
    total_sum = sum(A)
    for i in range(1, len(A)):
#        print 'Checking i==%d, A[i]==%d...' % (i, A[i])
        diff = abs(left_sum - (total_sum - left_sum))
#        print 'left_sum(%d) - right_sum(%d) = diff(%d)' % (left_sum, total_sum - left_sum, diff)
        if diff < min_diff:
#            print 'New diff of', diff
            min_diff = diff
#        else:
#            print 'Old diff stays:', min_diff
        left_sum += A[i]
    return min_diff

#input = [858, 738, 134, -42, 329, 825, -4, 535, 969, -651, 744, 485, -283, 9, -683, 725, -681, 59, -138, -821, -65, -938, -972, 300, -246, -275, -561, 31, 306, -396, -13, -698, 667, 585, -759, 220, 942, -967, 180, -532, 143, -531, -376, 883, -459, -115, -821, -801, 831, 617, -84, -396, -919, -199, -214, -997, 240, -727, 309, 989, 208, -614, -570, -470, 788, 881, -145, -363, 33, 552, -145, -175, -950, -296, 461, 314, -121, 961, 448, 119, 314, 152, 543, 121, 365, -136, 401, -992, 603, 561, -271, 796, 175, -167, -177, 638, -22, 207, -814, 762]
#input = [3, 1, 2, 4, 3]

print solution(input)