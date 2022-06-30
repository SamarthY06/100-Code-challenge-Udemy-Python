def prefix(s,p):
    prefix = True
    if len(p) <= len(s):
      for i in range(len(p)):
        if s[i]!=p[i]:
            prefix = False
      
        else:
            continue
      print(prefix)
    else:
      print("False")

prefix("Nora","Circum")
  