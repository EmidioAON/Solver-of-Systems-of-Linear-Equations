import softposit as sp
import numpy as np
import random

def PerformOperation(a, n):

	flag = 0
	i = 0
	for cont in range(0,n):

		if (a[i][i] == 0):
			c = 1
			while (((i + c) < n) and (a[i + c][i]) == 0):
				c = c + 1
				pass
			if ((i + c) == n):
				flag = 1
				break;
				pass
			j = i;
			k = 0;
			for cont2 in range(0,n+1):
				temp 	  = a[j][k]
				a[j][k]   = a[j+c][k]
				a[j+c][k] = temp

				k = k + 1
				pass
			pass

		j = 0
		for cont3 in range(0,n):
			if (i != j):
				pro = ((a[j][i])/(a[i][i]))
				k = 0
				for cont4 in range(0,n+1):
					a[j][k] = a[j][k] - ((a[i][k]) * pro);
					k = k + 1
					pass
				pass

			j = j + 1
			pass

		i = i + 1
		pass


	return flag
	pass

def CheckConsistency(a, n, flag):
	flag = 3

	i = 0
	for cont in range(0,n):
		sum = 0
		j = 0
		for cont2 in range(0,n):
			sum = sum + a[i][j];
			j = j + 1
			pass
		if (sum == a[i][j]):
			flag = 2
			pass
		i = i + 1
		pass

	return flag
	pass

def PrintResult(a, n, flag):

	if (flag == 2):
		print('Infinite Solutions Exists')
		pass
	else:
		if (flag == 3):
			print('No Solution Exists')
			pass
		else:
			i = 0
			print('Matriz Final')
			for cont in range(0,n):
				print(a[i]/a[i][i])
				i = i + 1
				pass
			print(' ')
			pass

	pass

#main

n = random.randint(1,10)
a = np.full( (n,n+1), sp.posit32(0) )
b = np.full( (n,n+1), 0, float )


j = 0
for cont3 in range(0,n):
		k = 0
		for cont4 in range(0,n+1):
			num = random.randint(0,999)
			a[j][k] = sp.posit32(num)
			b[j][k] = num
			k = k + 1
		pass
		j = j + 1
pass

print("Matriz inicial:\n{matriz}\n".format(matriz = a) )

flag_a = PerformOperation(a, n)
	
if (flag_a == 1):
	flag_a = CheckConsistency(a, n, flag_a)

PrintResult(a, n, flag_a)