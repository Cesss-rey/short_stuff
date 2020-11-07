def saluda_amigos():
	print("A cuantos amigos quieres saludar?? ")
	
	no_amigos = int(input())
	amigos = []

	for x in range(1,no_amigos+1):
		#amigos.append(input(f"cual es tu amigo {x}??"))
		amigo = input(f"cual es tu amigo {x}??")
		print(amigo)		

	print("el programa termino")

saluda_amigos()