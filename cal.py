def sum(a,b):
	print(a+b)
def sub(a,b):
	print(a-b)
def mul(a,b):
	print(a*b)
def div(a,b):
	print(a/b)
def inputdetails():
	a=int(input("enter a"))
	b=int(input("enter b"))
	ch=mychoice()
	if(ch==1):
		sum(a,b)
	elif(ch==2):
		sub(a,b)
	elif(ch==3):
		mul(a,b)
	elif(ch==4):
		div(a,b)
	else:
		print("invalid choice")
def mychoice():
	print("1:Addition")
	print("2:Substraction")
	print("3:Multiplication")
	print("4:Division")
	ch=int(input("enter choice:"))
	return ch
inputdetails()
mychoice()


