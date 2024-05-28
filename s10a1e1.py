# Solicita ao usuário para inserir um número
numero = int(input("Digite um número para ver a sua tabela de multiplicação: "))

# Laço for para percorrer de 1 a 10
for i in range(0, 10):
    # Calcula o produto do número fornecido pelo valor atual do laço
    produto = numero * i
    # Imprime o produto em uma nova linha
    print(f"{numero} x {i} = {produto}")
