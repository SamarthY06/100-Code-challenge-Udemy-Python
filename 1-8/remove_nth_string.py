def remove(s,i):
    
    if i >= len(s):
        print("out of order")
    elif i == None:
        print("Empty string")
    else:
        string = s.replace(s[i],'')
        print(string)
remove("Hello",1)
    