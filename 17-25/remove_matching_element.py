def remove(l,n):
    b = []
    if (len(l)==0):
        print("Empty List")
    else:
        for i in range(len(l)):
        
          if (l[i]!=n and n in l):
             b.append(l[i]) 
          elif(l[i]!=n and n not in l):
            print("Not found")  
          else:
            continue
    if(b!=[]):
      print(b)

           
remove([],4)
            
    
