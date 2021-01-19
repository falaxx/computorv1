import sys
import numpy as np
import os

def exit(error):
	if error == 0:
		print("should finish with X^")
	if error == 1:
		print("operators should be alone ")
	if error == 2:
		print("X should be followed by ^ and preceded by *")
	if error == 3:
		print("^ should be followed by 0 1 2 or 3 and preceded by X ")
	if error == 4:
		print("- or + should be followed by one space then a number")
	if error == 5:
		print("* should be followed by one space then X")
	if error == 6:
		print("wrong float ")
	if error == 7:
		print("number should be followed by * ")
	if error == 14:
		print("Wrong entry")
	if error == 8:
		print("All reel number are solution")
	if error == 9:
		print("There is no solution")
	if error == 10:
		print("Polynomial degree: 3")
		print("Can't compute degree three")
	if error == 11:
		print("Too much minus in a row")
	if error == 12:
		print("Error with minus sign")
	os._exit(os.EX_OK)



def check(s):
	s.replace('\t',' ')
	s1 = s.split()
	if (s1[len(s1)-1].find("X^") == -1):
		exit(0)
	for i in range(0,len(s1)):
		for j in range(0,len(s1[i])):
			if s1[i][0].isdigit():
				if (i +1 > len(s1) or s1[i+1][0] != "*"):
					exit(7)
			if (s1[i][j] == "."):
				test = s1[i]
				if s1[i][0] == "-":
					test = test.replace(s1[i][:1], '')
				test = test.split(".")
				if (len(test)!= 2 or test[0].isnumeric() == False or test[1].isnumeric() == False):
					exit(6)
			if ((s1[i][j] == "+" or s1[i][j] == "*") and (len(s1[i]) != 1)):
				exit(1)
			if (s1[i][j] == "-" and j != 0):
				exit(4)
			if (s1[i][j] == "-" and len(s1[i]) != 1 and (s1[i][j+1].isdigit() == False or s1[i+1][0]!= '*')):
				exit(12)
			if (s1[i][j] == "-" and (len(s1[i]) == 1) and (s1[i+1][0].isdigit() == False and s1[i+1][0] != "-" )):
				exit(12)
			if (s1[i][j] == "-" and (len(s1[i]) == 1) and s1[i+1][0] == "-" and len(s1[i+1]) == 1):
				exit(12)
			if (s1[i][j] == "-" and len(s1) > i+1 and s1[i+2][0] == "-"):
				exit(11)
			if (s1[i][j] == "+" and ((s1[i+1][0] == "-" and len(s1[i+1]) <= 1) or (s1[i+1][0].isdigit() == False and s1[i+1][0] != "-"))):
				exit(4)
			if ((s1[i][j] == "*") and s1[i+1][0] != "X"):	
				exit(5)
			if ((i == 0 and s1[i][j] == "*") or (i > 1 and s1[i][j] == "X" and s1[i-1][0] != "*")):
				exit(5)
			if (s1[i][j] == "X"):
				if ((j + 1 < len(s1[i]) and s1[i][j+1] != "^") or (j + 1 >= len(s1[i])) or i == 0):
					exit(2)
			if (s1[i][j] == "^"):
				if (j != len(s1[i]) -2 or ( s1[i][j+1] != "1" and s1[i][j+1] != "2" and s1[i][j+1] != "0" and s1[i][j+1] != "3")):
					exit(3)
	
def verif_str(s):
	for j in range (0,len(s)):
		for i in range(0,len(s[j])):
			if(s[j][i].isdigit() == False and s[j][i]!= "-" and s[j][i]!= "." and s[j][i]!= "*" and s[j][i]!= "+" and s[j][i]!= "X" and s[j][i]!= "^" and s[j][i]!= " " and s[j][i]!= "\t"):
				exit(14)
    
def simplify(s, abc):
	tmp = np.zeros(1)
	neg = 0
	s1 = s[0].split()
	s2 = s[1].split()
	for i in range(0,len(s1)):
		if (s1[i][0].isdigit()  == True):
			tmp = float(s1[i])
			if neg == 1:
				tmp = tmp * -1
				neg = 0
		if (s1[i][0] == "-" ):
			if (len(s1[i]) == 1):
				neg = 1	
			if len(s1[i])!=1:
				tmp = float(s1[i])
				if neg == 1:
					tmp = -tmp
					neg = 0
		if (s1[i] == "X^0"):
			abc[2] += tmp
			tmp = 0
		if (s1[i] == "X^1"):
			abc[1] += tmp
			tmp = 0
		if (s1[i] == "X^2"):
			abc[0] += tmp
			tmp = 0
		if (s1[i] == "X^3"):
			abc[3] += tmp
			tmp = 0

	tmp = 0
	neg = 0
	for i in range(0,len(s2)):
		if (s2[i][0].isdigit()  == True):
			tmp = float(s2[i])
			if neg == 1:
				tmp = tmp * -1
				neg = 0
		if (s2[i][0] == "-" ):
			if (len(s2[i]) == 1):
				neg = 1	
			if len(s2[i])!=1:
				tmp = float(s2[i])
				if neg == 1:
					tmp = -tmp
					neg = 0
		if (s2[i] == "X^0"):
			abc[2] -= tmp
			tmp = 0
		if (s2[i] == "X^1"):
			abc[1] -= tmp
			tmp = 0
		if (s2[i] == "X^2"):
			abc[0] -= tmp
			tmp = 0
		if (s2[i] == "X^3"):
			abc[3] -= tmp
			tmp = 0			
	print("reduced form")
	str1 = str(abc[1])
	str0 = str(abc[0])
	str2 = ""
	if abc[3] != 0:
		if (abc[3] > 0):
			str2 =  "+ " + str(abc[3]) + " * X^3 "
		else:
			str2 = str(abc[3]) + " * X^3 "
	if (abc[1] >= 0):
		str1 = "+ " + str1
	if (abc[0] >= 0):
		str0 = "+ " + str0
	if (abc[3] == 0):
		if (abc[0] == 0):
			if (abc[1] == 0):
				if (abc[2] == 0):
					print ("0 = 0")
					return abc
				print(str(abc[2]) + " * X^0 " + "= 0")
				return abc
			print(str(abc[2]) + " * X^0 " + str1 + " * X^1 " + "= 0")
			return abc
		print(str(abc[2]) + " * X^0 " + str1 + " * X^1 " + str0 + " * X^2 " + "= 0")
		return abc
	print(str(abc[2]) + " * X^0 " + str1 + " * X^1 " + str0 + " * X^2 " + str2 + "= 0")
	if abc[3] != 0:
		exit(10)
	return abc

def abs_(number):
	if (number < 0):
		number = number * - 1
	return number

def degree(abc):
	if abc[3] == 0:
		if abc[0] == 0:
			if abc[1] == 0:
				if abc[2] == 0:
					print("Polynomial degree: 0")
					return
				print("Polynomial degree: 0")
				return
			print("Polynomial degree: 1")
			return
		print("Polynomial degree: 2")
		return
	print("Polynomial degree: 3")
	return
				


def solve(s, abc):
	degree(abc)
	if (abc[0] == 0 and abc[1] == 0 and abc[2] == 0):
		exit(8)
	if (abc[0] == 0):
		if (abc[1] == 0):
			exit(9)
		print ("x = " + str(-abc[2] / abc[1]))
		exit(42)
	delta = abc[1] * abc[1] - 4 * abc[0] * abc[2]
	print("Delta = " + str(delta))
	if delta > 0:
		print("There are two solutions:")
		x1 = (-1 * abc[1] - delta ** 0.5) / (2 * abc[0])
		x2 = (-1 * abc[1] + delta ** 0.5) / (2 * abc[0])
		print ("x1 = " + str(x1) + " x2 = " + str(x2))
	if delta < 0:
		print("There are two solutions:")
		if (((abs(delta) ** 0.5) / (2 * abc[0])) < 0):
			print("x1 = " + str((-1 *abc[1]) / (2 * abc[0])) + " " + str((abs_(delta) ** 0.5) / (2 * abc[0])) + "i")
			print("x2 = " + str((-1 *abc[1]) / (2 * abc[0])) + " +" + str(-(abs_(delta) ** 0.5) / (2 * abc[0])) + "i")
		else:
			print("x1 = " + str((-1 *abc[1]) / (2 * abc[0])) + " +" + str((abs_(delta) ** 0.5) / (2 * abc[0])) + "i")
			print("x2 = " + str((-1 *abc[1]) / (2 * abc[0])) + " " + str(-(abs_(delta) ** 0.5) / (2 * abc[0])) + "i")
	if delta == 0:
		print("There is one solution:")
		x1 = -1 * abc[1] / (2 * abc[0])
		print("x = " + str(x1))
		
def compute(s):
	try:
		abc = np.zeros(4)
		verif_str(s)
		check(s[0])
		check(s[1])
		abc = simplify(s,abc)
		solve(s,abc)
	except:
		exit(14)

def main():
	try:
		if len(sys.argv) == 2 :
			str_arg = sys.argv[1]
			str_arg = str_arg.split("=")
			if(len(str_arg) == 2):
				str_arg[0] = str_arg[0].strip()
				str_arg[1] = str_arg[1].strip()
				compute(str_arg)
			else:
				print("Wrong number of arguments")
		else:
			print("Need exactly one argument : the polynomial equation")
	except:
		print("Error")
		return

if __name__ == "__main__":
	main()
