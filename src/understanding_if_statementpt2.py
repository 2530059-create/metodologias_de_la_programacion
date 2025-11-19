"""
vamos a realizar un programa que pregunte al usuario 
por su edad y muestre un mensaje diferente segun el rango de edad

"""
#>#<

#try:
    #age=int(input("introduce tu edad: "))
   # if age >= 18:
    #  print ("eres mayor de edad")
    #elif age <=18:
     #  print("aun eres menor de edad")
#except: print("tuviste error al ingresar tu edad")

#print ("hola julian")


try:
 age=int(input("introduce tu edad: "))

    if age >= 100:
      print("tines mas de un siglo de edad")
    elif age >= 18 and age <=99:
      print ("eres mayor de edad")
    elif age >0 and age<18:
     print ("eres menor de edad")
    else:
     print ("tuviste un error")
except: 



#multiple if

guiso