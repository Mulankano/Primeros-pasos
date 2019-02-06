
num1=int(input("Introduzca primer número a comparar: "))
num2=int(input("Introduzca segundo número a comparar: "))

def DevuelveMax (n1, n2):
	if n1>n2:
		print (n1)
	elif n1<n2:
		print (n2)
	else:
		print("Son iguales")

print("El número mas alto es: ")
DevuelveMax(num1, num2)





