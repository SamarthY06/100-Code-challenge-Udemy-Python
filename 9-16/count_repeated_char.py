def repeated(s):
    counter = 0
    b= []
    for i in range(len(s)-1):
        for j in range(len(s)-i):
            if j!=0:
              if (s[i]==s[i+j]):
                counter+=1
                b.append(s[i])
    x = sorted(set(b))
    print(len(set(b)))
    print(x,end = ' ')

repeated("Hello")