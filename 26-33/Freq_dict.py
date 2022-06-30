def frequency(l):
    l_sort = list(set(l))
    freq = {}
    for i in range(len(l_sort)):
      freq[f'{l_sort[i]}'] = f'{l.count(l_sort[i])}'

    print(freq)

frequency(["a","a","b","c","a","b"])