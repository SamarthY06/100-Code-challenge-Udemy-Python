def comman(l_1,l_2):
    b = []
    for i in l_2:
        if i in l_1:
            b.append(i)

    print(b)
        
comman([4,5,6],[1,4,5])