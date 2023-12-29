#Gauss elimination
#Perform operations: scalar multiply, subtract/add rows, interchange rows

import numpy as np
import pandas as pd

#Input matrix:
print("Enter matrix: ")
rows = list()
while True:
	row = input().split()
	row = [int(x) for x in row]
	if len(row) == 0:
		break
	rows.append(np.array(row))


for i in range(1, len(rows)):
	for j in range(0, i):
		rows[i] = rows[i] - (rows[j])*(rows[i][j]/rows[j][j])

df = pd.DataFrame(rows)
print(df)

# If consistent and unique solution:
n = len(rows[0]) - 1
x = [None]*n
for i in range(n-1, -1, -1):
	x[i] = rows[i][-1]
	for j in range(i+1, n):
		x[i] = x[i] - (x[j]*rows[i][j])
	x[i] = x[i]/rows[i][i]
	# print(i)
	# print(x)

print(x)