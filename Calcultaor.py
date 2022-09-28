

import time
import math

print("\n\n")

print("\t\t\t--------------------------------\\** Calculator **\\-----------------------------")

print("\n\n")
FM = input("\t\t\tChoose F\\M(F = Female,M = Male) ::")
print("\n\n")




user_nam = str(input("\t\t\tEnter Name ::: "))

upp_nam = user_nam.upper()
print("\n\n")

print("\t\t\t\t\tProcessing......................")
time.sleep(1)

print("\n")

if FM == "M":


	print("\t\t\t** WELCOME {} SIR TO OUR CALCULATOR **".format(upp_nam))

elif FM == "F":

	print("\t\t\t** WELCOME {} MAM TO OUR CALCULATOR **".format(upp_nam))
print("\n\n")
time.sleep(3)
print("\n\n")
print("\t\t\t||                  LET's START                 ||")
print("\n\n")
time.sleep(3)

OP = input("\t\t\tChoose Operator (+,-,X,/,%) ::: ")
print("\n\n")
print("\t\t\t\t\tProcessing.......................")
time.sleep(4)


print("\n\n")


print("\t\t\t** YOU CHOOSE << {} >> OPERATOR GREAT !!!! ** ".format(OP))

print("\n\n")
time.sleep(4)

user_num1 = int(input("\t\t\tEnter Num1 ::: "))

print("\n")

user_num2 = int(input("\t\t\tEnter Num2 ::: "))

print("\n")


if OP == "+":

	sum_num = user_num1+user_num2

	print("\t\t\t\t\t*******************************")
	print("\t\t\t\t\t*                             *")
	print("\t\t\t\t\t*   {}  +  {}   = {}          *".format(user_num1,user_num2,sum_num))
	print("\t\t\t\t\t*                             *")
	print("\t\t\t\t\t*******************************")
	print("\n\n")

elif OP == "-":

	minu_num = user_num1-user_num2
	print("\t\t\t\t\t*******************************")
	print("\t\t\t\t\t*                             *")
	print("\t\t\t\t\t*  {} - {}   =  {}            *".format(user_num1,user_num2,minu_num))
	print("\t\t\t\t\t*                             *")
	print("\t\t\t\t\t*******************************")
	print("\n\n")

elif OP == "X":

	multi_num = user_num1*user_num2

	print("\t\t\t\t\t*******************************")
	print("\t\t\t\t\t*                             *")
	print("\t\t\t\t\t*  {} X {}   = {}             *".format(user_num1,user_num2,multi_num))
	print("\t\t\t\t\t*                             *")
	print("\t\t\t\t\t*******************************")
	print("\n\n")


elif OP == "/":

	divi_num = user_num1/user_num2


	print("\t\t\t\t\t*******************************")
	print("\t\t\t\t\t*                             *")
	print("\t\t\t\t\t*  {} / {}   =  {}            *".format(user_num1,user_num2,divi_num))
	print("\t\t\t\t\t*                             *")
	print("\t\t\t\t\t*******************************")
	print("\n\n")


elif OP == "%":

	remi_num = user_num1%user_num2

	print("\t\t\t\t\t*******************************")
	print("\t\t\t\t\t*                             *")
	print("\t\t\t\t\t*  {} % {}   =  {}            *".format(user_num1,user_num2,remi_num))
	print("\t\t\t\t\t*                             *")
	print("\t\t\t\t\t*******************************")
	print("\n\n")






time.sleep(3)

print("\t\t\t--------------------------------\\** Thank you **\\-----------------------------")

print("\n\n\n\n")





