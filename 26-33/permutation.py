from itertools import permutations
def permutation(l):
    p = permutations(l)
    for i in list(p):
        print(i)

permutation([1,2,3])