from os import remove


def difference(l_1,l_2):
    b = []
    if l_1 is []:
        print(l_1)
    else:
        for i in l_2:
            if i in l_1:
                l_1.remove(i)
    print(l_1)
        
difference([1,2,3,4],[2,3])
