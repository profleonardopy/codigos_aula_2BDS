import time

# Lista com números de 0 a 999999
lista = list(range(1000000))

start_time = time.time() # Tempo inicial

# Laço while refatorado para usar list comprehension
lista = [x for x in lista if x % 2 == 0] # Mantém apenas números pares

end_time = time.time() # Tempo final


print(f"Tempo de execução: {end_time - start_time} segundos.")
