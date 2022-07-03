c = []
f = {}
def sort(d):
    b = list(d.keys())
    a = list(d.values())
    for i in a:
        c.append(sorted(i))
    for i in range(len(c)):
        f[b[i]] = c[i]
 
    print(f)

sort({
	"a": [4, 3, 2],
	"b": [5, 3, 7],
	"c": [1, 9, 10],
	"d": [3, 4, 1]
})