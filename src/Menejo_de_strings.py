full_name = input("Ingrese su nombre completo: ")

full_name= full_name.strip()

if full_name==" ":
    print ("debes de ingresar un nombre valido")

words= full_name.split()

"""
el split sirve para poder separar los caracteres de algo
por ejemplo full_name .split = ["JULIAN" "CARMONA"]
"""
if len (words) <2:
    print("debes de poner un nombre valido")

"""
el len sirve para que cuente la cantidad de caracteres de una palabra
por ejemmplo julian las salidas van a ser "6"
"""

formatted_name = " ".join(words).title()
initials = ""

for w in words:
    initials += w[0].upper() + "."

print("Formatted name:", formatted_name)
print("Initials:", initials)

