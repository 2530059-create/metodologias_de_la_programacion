"inicio de tarea"
try:
   
   age= int(input("Ingresa tu edad: "))
   if age<= 4:
    print ("Tu entrada es gratis")
   elif age >4 and age <=18:
    print("Tu entrada tiene un costo de $200")
   elif age >18:
    print("Tu entrada tiene un costo de $400")
except: print ("tuviste un error al ingresar tu edad")
"listo"