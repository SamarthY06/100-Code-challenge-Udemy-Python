def check(string):
    l = ["a","e","i","o","u"]
    for s in string:
       if(s.isalpha()):
            if s in l :
                print(f'{s} is a vowel')
            else:
                print(f'{s} is a consonent')
       else:
           print(f'{s} is not a letter')


check("Score: 36")