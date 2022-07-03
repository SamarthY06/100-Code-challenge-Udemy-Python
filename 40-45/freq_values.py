def freq(d):
    a = list(d.values())
    b = list(set(a))
    dct = {}
    for i in range(len(b)):
        dct[f'{b[i]}'] =  a.count(b[i])

    print(dct)

freq({
	"a": 4,
	"b": 4,
	"c": 2,
	"d": 7,
	"e": 4,
	"f": 2,
	"g": 7,
	"h": 7
 })