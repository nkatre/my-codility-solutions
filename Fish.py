# 37 in 14min https://codility.com/demo/results/demoPF93WA-PHW/
# 100 I assume by http://codesays.com/2014/solution-to-fish-by-codility/

def solution(A, B):
    alive_count = 0        # The number of fish that will stay alive
    downstream = []        # To record the fishs flowing downstream
    downstream_count = 0   # To record the number of elements in downstream
 
    for index in xrange(len(A)):
        # Compute for each fish
        if B[index] == 1:
            # This fish is flowing downstream. It would 
            # NEVER meet the previous fishs. But possibly
            # it has to fight with the downstream fishs.
            downstream.append(A[index])
            downstream_count += 1
        else:
            # This fish is flowing upstream. It would either
            #    eat ALL the previous downstream-flow fishs,
            #    and stay alive.
            # OR
            #    be eaten by ONE of the previous downstream-
            #    flow fishs, which is bigger, and died.
            while downstream_count != 0:
                # It has to fight with each previous living
                # fish, with nearest first.
                if downstream[-1] < A[index]:
                    # Win and to continue the next fight
                    downstream_count -= 1
                    downstream.pop()
                else:
                    # Lose and die
                    break
            else:
                # This upstream-flow fish eat all the previous
                # downstream-flow fishs. Win and stay alive.
                alive_count += 1
 
    # Currently, all the downstream-flow fishs in stack 
    # downstream will not meet with any fish. They will
    # stay alive.
    alive_count += len(downstream)
 
    return alive_count

def mySolution(A, B):
    # write your code in Python 2.6
    upstream_fish_count = sum(1 for b in B if b == 0)
    downstream_fish_count = len(A) - upstream_fish_count
    potential_collisions = 0
    counts = [0] * len(A)
    downstream_fish_stack = []
    for idx, _ in enumerate(A):
        if B[idx] == 0:
            upstream_fish_count -= 1
        if B[idx] == 1:
            potential_collisions += upstream_fish_count

    return potential_collisions


print solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0])