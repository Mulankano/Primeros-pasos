
arro=0
punt=0
email=input("Introduzca su dirección de correo: ")

for i in email:
	if i=="@":
		arro=arro+1
	elif i==".":
		punt=punt+1

if arro==1 and punt>0:
	print("email correcto")
else:
	print("email incorrecto")


