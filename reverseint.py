number=int(input("enter the integer number:"))
revs_number=0
while(number>0):
	reminder=number%10
	revs_number=(revs_number*10)+reminder
	number=number//10
print("the reverse number is:{}".forma(revs_number))