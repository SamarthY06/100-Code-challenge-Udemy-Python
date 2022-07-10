from cmath import sqrt


def quadratic(a,b,c):
    D=b**2 - 4*a*c
    if D > 0:
        x1 = (-b - sqrt(D))/(2*a)
        x2 = (-b + sqrt(D))/(2*a) 
        print(x1,x2)
    if D == 0:
        x2 = -b/(2*a)
        print(x2)
    if D <0:
        print("Complex Number")

quadratic(1,2,1)