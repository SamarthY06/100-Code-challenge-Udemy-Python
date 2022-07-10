def calculator(a,b,c):
    if c == 1:
        print (a+b) 
    if c == 2:
        print (a-b)
    if c == 3:
        print (a*b)
    if c == 4:
        print (a/b)
    if c == 5:
        print (int(a/b))
    if c == 6:
        print (a%b)   


print("Enter the first number")
a = int(input())
print("Enter the second number")
b = int(input())
l = ["Addition","Substraction","Multiplication","Division","Integer Division","Modulo"]
print('These are the options available:')
for i in range(len(l)):
    print(f'{i+1} - {l[i]}')
print("Enter the corresponding number")
c = int(input())
print(calculator(a,b,c))