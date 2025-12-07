# pregunta de rescate: Serie Fibonacci
"""
try:
    n = int(input("Cuantos términos quieres: "))
except:
    print("Entrada inválida")
    quit()

if n <= 0:
    print("El número debe ser mayor que 0")
    quit()

a = 0
b = 1

print("Serie Fibonacci:")

contador = 1
while contador <= n:
    print(a)
    temp = a
    a = b
    b = temp + b
    contador += 1
"""

# CRUD super simple pero usando funciones
"""
students = {}   # estructura en memoria

def create_student():
    id = input("ID: ")
    name = input("Name: ")
    students[id] = name
    print("Student added.")

def read_students():
    if not students:
        print("No data.")
    else:
        for name in students.values():   
            print(name)

def update_student():
    id = input("ID to update: ")
    if id in students:
        new_name = input("New name: ")
        students[id] = new_name
        print("Updated.")
    else:
        print("ID not found.")

def delete_student():
    id = input("ID to delete: ")
    if id in students:
        del students[id]
        print("Deleted.")
    else:
        print("ID not found.")

# Menú principal
while True:
    print("\n MENU ")
    print("1. Create")
    print("2. Read")
    print("3. Update")
    print("4. Delete")
    print("5. Exit")

    choice = input("Choose: ")

    if choice == "1":
        create_student()
    elif choice == "2":
        read_students()
    elif choice == "3":
        update_student()
    elif choice == "4":
        delete_student()
    elif choice == "5":
        break
    else:
        print("Invalid option.")
"""

# Problem 2: Rectangle area and perimeter

"""def calculate_area(width, height):
    return width * height

def calculate_perimeter(width, height):
    return 2 * (width + height)

# Lectura de datos
try:
    width = float(input("Width: "))
    height = float(input("Height: "))
except ValueError:
    print("Error: invalid input")
    exit()

# Validaciones
if width <= 0 or height <= 0:
    print("Error: invalid input")
else:
    print("Area:", calculate_area(width, height))
    print("Perimeter:", calculate_perimeter(width, height))
"""

# Problem 1: Average of numbers with while and sentinel

"""sentinel = -1   # valor fijo en el código
count = 0
total = 0.0

while True:
    user_input = input("Enter a number (-1 to stop): ")

    # Intentar convertir a float
    try:
        num = float(user_input)
    except ValueError:
        print("Invalid input, try again.")
        continue

    # Si es el centinela se detiene el ciclo
    if num == sentinel:
        break

    # Acumular valores válidos
    total += num
    count += 1

# Mostrar resultados
if count == 0:
    print("Error: no data")
else:
    average = total / count
    print("Count:", count)
    print("Average:", average)
"""
n_terms = (input("Enter the number of terms: "))

try:
    n = int(n_terms)
    if n < 1 or n > 50:
        print("Error: invalid input")
        exit()
except ValueError:
    print("Error: invalid input")
    exit()

fibonacci_series = []
a = 0
b = 1

for i in range(n):
    fibonacci_series.append(a)
    a, b = b, a + b

print(f"The Fibonacci Series is: {fibonacci_series}")