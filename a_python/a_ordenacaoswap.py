l_ordenar= [7, 3] 
print(f"Lista a ordenar= {l_ordenar}")

if l_ordenar[0] > l_ordenar[1]:
	swap= l_ordenar[0]
	l_ordenar[0]= l_ordenar[1]
	l_ordenar[1]= swap
print(f"Lista ordenada= {l_ordenar}")

