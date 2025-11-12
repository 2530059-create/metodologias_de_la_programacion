"""
las listas tambien pueder almacenar numeros y de echo 
son ideales para almacenarlos
 python ofrece cantidad de funciones integrados para trabajar con listas 
 de numeros.

 por ejemplo, funcion range()

 
"""
# la funcion range genera una lista de numeros en un rango especifico
# por ejemplo para generar un lista del uno al 9

numbers= list(range(10))
print (numbers)
print (type(numbers))

# Lo podemos realizar co un for loop:

for num in numbers:
    print(num)

# para seleccionar desde que numeros inicias y en cuale terminas
for num in range (1,8):
    print (num)

print("\n numeros impares")
# para que aparezcan los numeros impares del 1 al 9
for num in range(1,10,2): # son numeros impares
    print (num)

odd_numbers=list(range(1,10,20))
print(odd_numbers)

print("\n numeros pares")
# para numeros impares
for num in range (2,10,2):
    print (num)

even_numbers=list(range(2,10,2)) 
print(even_numbers)

# podemos crear cualquier de listas de numeros
# utilizando range () y lis ()

print("\n generar numeros al cuadrado ")

squares=[]
for num in range (1,11):
    square= num **2
    squares.append (square)
print(square)

print ("\n metodos built-in")

digits=[1,2,3,4,5,6,7,8,9,10]
print(f"lista de digitos: {digits}")
print ("valor minimo:", min(digits))
print ("valor maximo:", max(digits))
print ("valor de todos los numeros sumados:", sum(digits))













