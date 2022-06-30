def sort(s):
    b = ""
    splitted = s.split()
    for word in splitted:
        a = word.lower()
        sorted_txt = sorted(a)
        c = ''.join(sorted_txt)
        b+= c + ' '
    
    print(b.rstrip())

sort("Wonderful World")

