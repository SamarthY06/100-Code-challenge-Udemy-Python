def second_largest(l):
    b = list(set(l))
    b.sort()
    print(b[len(b)-2])


second_largest([1,2,3,4])