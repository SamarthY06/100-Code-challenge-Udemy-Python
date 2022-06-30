def reverse(s):
    b = ""
    splitted = s.split(" ")
    for word in splitted:
       rev = ''.join(reversed(word))
       swapcase = rev.swapcase()
       b += swapcase + ' '
    
    b.rstrip()
    print(b)

reverse("Hello World")