b = []
def max_sum(d):
    a = list(d.values())
    for i in range(len(a)):
        b.append(sum(a[i]))
    
    print(max(b))

max_sum({
	"a": [1, 2, 3],
	"b": [4, 0, -4],
	"c": [3, 5, 9],
	"d": [45, 12, 100]
})