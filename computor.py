import argparse
import sys
import numpy as np
import os
import math

def exit(error):
	if error == 0:
		print("should finish with X^")
	if error == 1:
		print("operators should be alone ")
	if error == 2:
		print("X should be followed by ^ and preceded by *")
	if error == 3:
		print("^ should be followed by 0 1 or 2 and preceded by X ")
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
	os._exit(os.EX_OK)



def check(s):
	stage = 0
	neg = 0
	s.replace('\t',' ')
	s1 = s.split()
	if (s1[len(s1)-1].find("X^") == -1):
		exit(0)
	for i in range(0,len(s1)):
		print(s1[i])
		for j in range(0,len(s1[i])):
			if s1[i][0].isdigit():
				if (i +1 > len(s1) or s1[i+1][0] != "*"):
					exit(7)
			if (s1[i][j] == "."):
				test = s1[i].split(".")
				if (len(test)!= 2 or test[0].isnumeric() == False or test[1].isnumeric() == False):
					exit(6)
			if ((s1[i][j] == "-" or s1[i][j] == "+" or s1[i][j] == "*") and (len(s1[i]) != 1)):
				exit(1)
			if ((s1[i][j] == "-" or s1[i][j] == "+") and s1[i+1][0].isdigit() == False):
				exit(4)
			if ((s1[i][j] == "*") and s1[i+1][0] != "X"):	
				exit(5)
			if ((i == 0 and s1[i][j] == "*") or (i > 1 and s1[i][j] == "X" and s1[i-1][0] != "*")):
				exit(5)
			if (s1[i][j] == "X"):
				if ((j + 1 < len(s1[i]) and s1[i][j+1] != "^") or (j + 1 >= len(s1[i])) or i == 0):
					exit(2)
			if (s1[i][j] == "^"):
				if (j != len(s1[i]) -2 or ( s1[i][j+1] != "1" and s1[i][j+1] != "2" and s1[i][j+1] != "0")):
					exit(3)
			if (s1[i][j] == "-"):
				neg = 1
		# print(s1[i])
	
def verif_str(s):
	for j in range (0,len(s)):
		for i in range(0,len(s[j])):
			print(s[j][i])
			if(s[j][i].isdigit() == False and s[j][i]!= "-" and s[j][i]!= "." and s[j][i]!= "*" and s[j][i]!= "+" and s[j][i]!= "X" and s[j][i]!= "^" and s[j][i]!= " " and s[j][i]!= "\t"):
				exit(14)
    
def simplify(s, abc):
	tmp = np.zeros(1)
	neg = 0
	stage = 0
	s1 = s[0].split()
	s2 = s[1].split()
	for i in range(0,len(s1)):
		# print(s1[i])
		if (s1[i][0].isdigit()  == True):
			tmp = float(s1[i])
			if neg == 1:
				tmp = tmp * -1
				neg = 0
			print (tmp)
		if (s1[i][0] == "-" ):
			neg = 1
		if (s1[i] == "X^0"):
			abc[2] += tmp
			tmp = 0
		if (s1[i] == "X^1"):
			abc[1] += tmp
			tmp = 0
		if (s1[i] == "X^2"):
			abc[0] += tmp
			tmp = 0

	tmp = 0
	neg = 0
	for i in range(0,len(s2)):
		print(s1[i])
		if (s2[i][0].isdigit()  == True):
			tmp = float(s2[i])
			if neg == 1:
				tmp = tmp * -1
				neg = 0
		if (s2[i][0] == "-" ):
			neg = 1
		if (s2[i] == "X^0"):
			abc[2] -= tmp
			tmp = 0
		if (s2[i] == "X^1"):
			abc[1] -= tmp
			tmp = 0
		if (s2[i] == "X^2"):
			abc[0] -= tmp
			tmp = 0
		print (tmp)
		
	print(abc)	
	print("reduced form")
	str1 = str(abc[1])
	str0 = str(abc[0])
	if (abc[1] >= 0):
		str1 = "+ " + str1
	if (abc[0] >= 0):
		str0 = "+ " + str0
	print(str(abc[2]) + " * X^0 " + str1 + " * X^1 " + str0 + " * X^2 = 0")
	return abc


def solve(s, abc):
	if (abc[0] == 0 and abc[1] == 0 and abc[2] == 0):
		exit(8)
	    #    b * b - 4 * a * c
	delta = abc[1] * abc[1] - 4 * abc[0] * abc[2]
	print("delta = " + str(delta))
	if delta > 0:
		print("there is two solutions")

		x1 = (-1 * abc[1] - math.sqrt(delta)) / (2 * abc[0])
		x2 = (-1 * abc[1] + math.sqrt(delta)) / (2 * abc[0])
		print ("x1 = " + str(x1) + " x2 = " + str(x2))
		# x1 = (- abc[1] - racinedelta) / 2a   (-b + racinedelta) / 2 
	if delta < 0:
		exit(9)
	if delta == 0:
		print("there is one solution")
		x1 = -1 * abc[1] / (2 * abc[0])
		print("x = " + str(x1))
		# -b / 2a 


	
		
def compute(s):
	abc = np.zeros(3)
	verif_str(s)
	check(s[0])
	# print("=")
	check(s[1])
	abc = simplify(s,abc)
	solve(s,abc)




def main():
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

if __name__ == "__main__":
	main()
