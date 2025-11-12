# list comprehasion 

"""
una list comprehension combina el for loop 
y la creacion de nuevos elementos en una 
sola linea de codigo y tambien, automaticamente 
agrega el nuevo elemento en la lista, es decir, 
sin utilizar el append 
"""

squares=[value**2 for num in range(10)]
print (squares)
# generando numeros pares con el if 
evens_list_compre=[value for value in range (0,10000)if value %2==0]
print (evens_list_compre)
