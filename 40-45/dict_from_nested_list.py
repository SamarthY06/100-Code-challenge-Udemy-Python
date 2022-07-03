d = {}
def nested_list(l):
    for i in range(len(l)):
            d[l[i][0]]= l[i][1]
    print(d)
    
nested_list([["a", 1], ["b", 2], ["c", 3], ["d", 4]])    