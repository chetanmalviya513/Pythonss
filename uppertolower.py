"""
x=input("enter value:")
y=""
for i in x:
	if ord(i)>=65 and ord(i)<=90:
		a=ord(i)+32
		b=chr(a)
		y=y+b
   	elif ord (i)>=97 and ord (i)<=122:
		y=y+i
	else:
		print("Invalid charecter")
		breack
print("value before conversion=",x)
print("value after conversion=",y)
"""
#SPECIAL CHARECTER 
"""
x=input("enter value:")

y=""
for i in x:
	if ord(i)>=65 and ord(i)<=90:
		a=ord(i)+32
		b=chr(a)
		y=y+b
	else:
		y=y+i	
print("value before conversion=",x)
print("value after conversion=",y)
"""

				#lower to upper

x=input("enter value:")
y=""
for i in x:
	if ord(i)>=65 and ord(i)<=122:
	a=ord(i)-32
	b=chr(a)
	y=y+b
	else:
	y=y+i
print("value before conversion=",x)
print("value after conversion=",y)
