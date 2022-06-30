def first3_last3(s):
    if(len(s)>6):
        print(s[0:3]+s[len(s)-3:len(s)])
    else:
        print("")

first3_last3("Amazing")