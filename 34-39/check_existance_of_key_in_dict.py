def check(d,key):
    if key in list(d):
        print(True)
    else:
        print(False)

check({"a":4,"b":5},"a")