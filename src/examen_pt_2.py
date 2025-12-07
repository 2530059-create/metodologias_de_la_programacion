#examen_version2c

#pregunta de rescate_1
""""
implementa un programa un programa de python que calcule y muestre la serie de fubunacci
"""""

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














