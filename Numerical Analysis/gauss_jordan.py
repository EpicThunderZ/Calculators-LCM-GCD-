# 1 0 0
# 0 1 0
# 0 0 1

# #go from 2nd row to last, 
# #2nd row = 2nd row - (1st element of 2nd row/1st element of 1st row)(1st row)
# 1 1 1
# 0 1 1
# 1 1 1
# #3rd row = 3rd row - (1st element of 3rd row/1st element of 1st row)(1st row)
# 1 1 1
# 0 1 1
# 0 1 1

# #3rd row = 3rd row - (2nd element of 3rd row/2nd element of 2nd row)(2nd row)
# #2nd row = 2nd row - (3rd element of 2nd row/3rd element of 3rd row)(3rd row)
# #

import numpy as np
import pandas as pd


rows = list()
while True:
	row = input().split()
	row = [int(x) for x in row]
	row = np.array(row)
	if len(row) == 0:
		break
	rows.append(row)

# df = pd.DataFrame(rows)
# print(df)

n = len(rows[0])
I = list()
for i in range(0, n):
	row = list()
	for j in range(0, n):
		if i == j:
			row.append(1)
		else:
			row.append(0)
	I.append(row)
I = [np.array(x) for x in I]

for i in range(1, len(rows)):
	m = i-1
	for j in range(i, len(rows)):
		if rows[j][i-1] > rows[m][i-1]:
			m = j
	temp = rows[i-1]
	tempI = I[i-1]
	rows[i-1] = rows[m]
	I[i-1] = I[m]
	rows[m] = temp
	I[m] = tempI


	for j in range(i, len(rows)):
		I[j] = I[j] - (I[i-1]*(rows[j][i-1]/rows[i-1][i-1]))
		rows[j] = rows[j] - (rows[i-1]*(rows[j][i-1]/rows[i-1][i-1]))
		
	for j in range(0, i):
		I[j] = I[j] - (I[i]*(rows[j][i]/rows[i][i]))
		rows[j] = rows[j] - (rows[i]*(rows[j][i]/rows[i][i]))

	# df = pd.DataFrame(rows)
	# print(df)

for i in range(0, len(rows)):
	I[i] = I[i]/rows[i][i]
	rows[i] = rows[i]/rows[i][i]

df = pd.DataFrame(rows)
print(df)
dfI = pd.DataFrame(I)
print(dfI)




