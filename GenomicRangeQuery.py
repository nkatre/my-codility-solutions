# 100 https://codility.com/demo/results/demoKZ973E-ACR/
# from http://codesays.com/2014/solution-to-genomic-range-query-by-codility/

# I was on my way there, thinking I'd include a 4-sized tuple in the counts...

def solution(S, P, Q):
    result = []
    DNA_len = len(S)
    mapping = {"A":1, "C":2, "G":3, "T":4}
    # next_nucl is used to store the position information
    # next_nucl[0] is about the "A" nucleotides, [1] about "C"
    #    [2] about "G", and [3] about "T"
    # next_nucl[i][j] = k means: for the corresponding nucleotides i,
    #    at position j, the next corresponding nucleotides appears
    #    at position k (including j)
    # k == -1 means: the next corresponding nucleotides does not exist
    next_nucl = [[-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len, [-1]*DNA_len]
 
    # Scan the whole DNA sequence, and retrieve the position information
    next_nucl[mapping[S[-1]] - 1][-1] = DNA_len-1
    for index in range(DNA_len-2,-1,-1):
        next_nucl[0][index] = next_nucl[0][index+1]
        next_nucl[1][index] = next_nucl[1][index+1]
        next_nucl[2][index] = next_nucl[2][index+1]
        next_nucl[3][index] = next_nucl[3][index+1]
        next_nucl[mapping[S[index]] - 1][index] = index
 
    for index in range(0,len(P)):
        if next_nucl[0][P[index]] != -1 and next_nucl[0][P[index]] <= Q[index]:
            result.append(1)
        elif next_nucl[1][P[index]] != -1 and next_nucl[1][P[index]] <= Q[index]:
            result.append(2)
        elif next_nucl[2][P[index]] != -1 and next_nucl[2][P[index]] <= Q[index]:
            result.append(3)
        else:
            result.append(4)
 
    return result
    

def MyPriorSolution(S, P, Q):
    string = list(S)
    running_totals = [0] * len(string)
    As = 0
    Cs = 0
    Gs = 0
    Ts = 0
    for idx, letter in enumerate(string):
        if letter == 'A':
            As += 1
            running_totals[idx] = As
        elif letter == 'C':
            Cs += 1
            running_totals[idx] = Cs
        elif letter == 'G':
            Gs += 1
            running_totals[idx] = Gs
        elif letter == 'T':
            Ts += 1
            running_totals[idx] = Ts

    print string
    print ['%d' % t for t in running_totals]
        
    results = [0] * len(P)
    for k, _ in enumerate(P):
        # get the sequence
        substring = string[P[k]:Q[k]]
        print k, P[k], Q[k], substring            
        # query S[Pk to Qk] for minimal nucleotide
            # Naive: loop through...

print solution ('GACACCATA', [0, 0, 4, 7], [8, 2, 5, 7])