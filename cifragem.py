import string

# Solicita ao usuário para inserir uma palavra
palavra = input("Digite uma palavra (sem pontuação): ")

# Dicionário para mapear letras para números
mapeamento = {chr(i + 96): i for i in range(1, 27)}

# Inicializa a string de resultado
resultado = ""

# Itera sobre cada caractere na palavra
for letra in palavra.lower():
    # Verifica se a letra está no dicionário (é uma letra do alfabeto)
    if letra in mapeamento:
        resultado += str(mapeamento[letra]) + " "

# Remove espaços em branco extras no final da string de resultado
resultado = resultado.strip()

# Imprime o resultado final
print("Cifra:", resultado)
