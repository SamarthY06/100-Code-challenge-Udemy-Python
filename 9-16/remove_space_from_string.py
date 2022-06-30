def remove_space(s):
    b = ""
    for i in range(len(s)):
      if s[i] != ' ':
        b = b + s[i]
      else:
        continue
    print(b)

remove_space("Hello this is Samarth")