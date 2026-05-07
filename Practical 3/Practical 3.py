import numpy as np

r, c = map(int, input().split())

arr = []
for i in range(r):
	row = list(map(int, input().split()))
	arr.extend(row)

a = np.array(arr).reshape(r, c)

print(a)
print(a.ndim)
print(a.shape)
print(a.size)