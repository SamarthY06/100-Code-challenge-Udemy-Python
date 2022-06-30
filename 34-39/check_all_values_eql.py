def check(d):
    if len(list(set(list(d.values())))) == 1:
        print(True)
    else:
        print(False)

check({"a":4,"b":4,"c":4})