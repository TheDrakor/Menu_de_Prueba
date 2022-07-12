#Pruebas

print("\n1.-Suma de 2 numeros")
print("\n2.-Sacar el area de un triangulo")
print("\n3.-Numero negativo o positivo")

op = ''

while op != "S":
	try:
		op = input("\n¿Que opcion eliges(presiona 's' para salir)?: ").upper()

		if int(op) == 1:
			n1 = float(input("Dame un numero: "))
			n2 = float(input("Dame otro numero: "))
			print(n1+n2)

		elif int(op)==2:
			base = float(input("Base ->"))
			altura = float(input("Altura ->"))
			print((base *altura)/2)

		elif int(op)==3:
			numero = float(input("Dame un numero: "))
			if numero>0:
				print("Es un numero positivo")
			elif numero<0:
				print("Es un numero negativo")
			else:
				print("El numero es cero")

	except ValueError:
		print("\nNo se permiten esos caracteres")
		
print("Gracias por participar!")