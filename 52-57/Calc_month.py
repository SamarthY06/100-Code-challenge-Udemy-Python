def month(m):
    days= [31,28,31,30,31,30,31,31,30,31,30,31]
    month = ["January","February","March","April","May","June","July","August","September","October","November","December"]
    for i in range(len(month)):
        if m == month[i]:
            print(f'{m}:{days[i]}')

month("February")
