def flat(l):
    b = []
    for i in l:
        if isinstance(i, int):
            b.append(i)
        else:
            for j in i:
                b.append(j)
        
    print(b)

flat([1,2,3,4,5,6,[7,8,9]])
