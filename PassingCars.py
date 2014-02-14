# https://codility.com/c/run/demoSPMPHQ-XZ8

# 66 23min https://codility.com/demo/results/demoSPMPHQ-XZ8/
# 100 https://codility.com/demo/results/demoMUSZ3W-KP6/

# Why not 100?  Didn't read the whole question and neglected to return -1 for passing_cars > 1,000,000,000.  No biggie.

from random import getrandbits

def solution(A):
        # Naive implementation, O(n^2)
    # Count the number of 0s
    # for each 0, count the number of 1s that follow it

    # keep a value cars_east
    # keep a value passing_cars
    # iterate through and...
        # when we find a 0, increase cars_east
        # when we find a 1, add cars_east to passing_cars
    cars_east = 0
    passing_cars = 0
    for car in A:
        if car == 0:
            cars_east += 1
        else:
            if passing_cars + cars_east > 1000000000:
                return -1
            passing_cars += cars_east
    return passing_cars

input = (int(getrandbits(1)) for i in range(100000))
print solution(input)