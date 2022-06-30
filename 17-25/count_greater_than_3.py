def county(l):
    count=0
    for i in l:
        if i>3:
            count+=1
        else:
            continue
    print(count)

county([1,2,3,4])