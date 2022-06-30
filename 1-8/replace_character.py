# without using replace function
# def replace(string,curr_char,new_char):
#     output=[]
#     for i in range(len(string)):
#         if string[i]!=curr_char:
#           output.append(string[i]) 
#         else:
#           output.append(new_char)
#     print(output)

# replace("Hello","l","s")

def replace(string,curr_char,new_char):
    output = ""
    for i in range(len(string)):
       if string[i]!=curr_char:
          output= output + string[i]
       else:
          output = output + new_char
    print(output)

replace("Hello","l","s")







replace("Hello","l","s")
