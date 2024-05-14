# Definimos uma variável nota
nota = 85

# Verificamos se a nota é maior ou igual a 90
if nota >= 90:
    print("Sua nota é A.")
# Verificamos se a nota é maior ou igual a 80 e menor que 90
elif nota >= 80:
    print("Sua nota é B.")
# Verificamos se a nota é maior ou igual a 70 e menor que 80
elif nota >= 70:
    print("Sua nota é C.")
# Verificamos se a nota é maior ou igual a 60 e menor que 70
elif nota >= 60:
    print("Sua nota é D.")
# Caso contrário (nota menor que 60)
else:
    print("Sua nota é F.")
