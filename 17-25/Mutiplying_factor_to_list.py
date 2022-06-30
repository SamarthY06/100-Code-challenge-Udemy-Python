def multiply(s,factor):
    output = []
    for i in range(len(s)):
      output.append(s[i] * factor)
    print(output)

multiply(['a','b','c','d'],3)