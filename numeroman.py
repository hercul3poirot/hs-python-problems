import random
n = 4
s = 25
R = 5.2 

import itertools

def findsubsets(s, n):
    return list(itertools.combinations(s,n))

possiblevals = [x for x in range(1, s+1)]

for i in findsubsets(possiblevals, n):
    if sum(i) == s:
        if max(i)/min(i) <= R:
            if i[0] + i[1] != i[2]:
                print(i)