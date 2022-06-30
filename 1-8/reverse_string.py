a = []
def reverse_string(string):
    for i in range(len(string)):
        a.append(string[len(string)-i-1])
        if i == len(string)-1:
            print(a)

reverse_string("Hello")    