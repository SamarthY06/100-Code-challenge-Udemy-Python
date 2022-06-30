def add(d,key,val):
    if key not in d:
       d[key]=val

    print(d)

add({"a":4,"b":5},"c",6)
