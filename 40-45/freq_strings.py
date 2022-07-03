
def freq(s):
    d = {}
    for char in s.lower():
        if char.isalpha():
            if char in d:
                d[char]+=1
            else:
                d[char]=1
    print(d)


freq("Hello World")
