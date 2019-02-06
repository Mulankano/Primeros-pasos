
def devuelve_ciudades(*ciudades):
	for elemento in ciudades:
		yield from elemento
ciudades=devuelve_ciudades("Madrid", "Barcelona")
print(next(ciudades))
print(next(ciudades))
