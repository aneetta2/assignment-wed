num=int(input("Enter a number"))
factorial=1
if num<0:
	print("factorial doesnt exit for negative numbers")
elif num==0:
	print("the factorial of zero is one")
else:
	for i in range(1,num+1):
		factorial=factorial*i
	print("The factorial of",num,"is",factorial)	