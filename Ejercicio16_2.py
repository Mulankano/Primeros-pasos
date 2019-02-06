

correcto=True
cont=0
password=input("Introduzco su contraseña: ")


for i in password:
	if i!=" ":
		cont=cont+1

	else:
		correcto=False

if correcto==True and cont>7:
	print("Contraseña correcta")
else:
	print("Contraseña incorrecta")

