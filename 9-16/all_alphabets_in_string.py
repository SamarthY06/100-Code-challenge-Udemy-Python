import string
def alphabet(s):
   a = s.lower()
   a = a.replace(' ','')
  
   b = 'abcdefghijklmnopqrstuvwxyz'
  
   if len(set(b))==len(set(a)):
    print("True")
   else :
    print("False")

alphabet("Hello")
   