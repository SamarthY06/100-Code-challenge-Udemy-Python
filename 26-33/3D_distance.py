from cmath import sqrt
import numpy as np
difference = []
def distance(A,B):
   import math
   for i in range(len(A)):
     difference.append(pow((A[i]-B[i]),2))
   
   print(sqrt(sum(difference)))

distance([3,4,5],[1,3,5])
