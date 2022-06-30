def withoutcommas(s):
  #print("".join(str(s).split(',')))   
  print(*s,sep='') 
    
withoutcommas([3,4,5,6])