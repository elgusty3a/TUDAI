forma = []

def pintar(forma):
	for b in range(forma[1]):
		for a in range(forma[0]):
			print (chr(0x2588),end="")
		print ()

''' definida la función ahora vamos a escribir una estructura 
que pida cantidad de columnas, que de una orden de arranque o fin,
y que tenga una x cantidad de intentos de arranque sino que corte
'''

colfil = input(f"Ingrese cant de columnas: ")
cf = int(colfil)
forma.append (cf)
colfil = input(f"Ingrese cant de filas: ")
cf = int(colfil)
forma.append (cf)
a = input(f"Ingrese orden de inicio: ")
c = 3 #cantidad de intentos despues del primer error de orden de inicio
while c!=0 and a!="exit":
	if a == "pinta":
#		print(forma) era para ver el arreglo y el orden en que guarda los datos
		pintar(forma)
		break
	else:
		print ("Orden invalida","\nRestan", c," intentos")
	c = c-1
	a = input(f"Ingrese orden de inicio: ")
	if c == 0:
		print ("Se han agotado los intentos")
if a=="exit": #si el usuario ingresa exit el programa termina
	breakpoint