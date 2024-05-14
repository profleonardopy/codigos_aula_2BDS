def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b != 0:
        return a / b
    else:
        return "Erro: Divisão por zero."

# Definimos as operações disponíveis em um dicionário
operacoes = {
    '+': somar,
    '-': subtrair,
    '*': multiplicar,
    '/': dividir
}

# Definimos os valores e a operação desejada
numero1 = 10
numero2 = 5
operacao = '*'

# Verificamos se a operação está presente no dicionário
if operacao in operacoes:
    # Se estiver, chamamos a função correspondente à operação
    resultado = operacoes[operacao](numero1, numero2)
    print(f"Resultado: {resultado}")
else:
    # Caso contrário, informamos que a operação não é válida
    print("Operação inválida.")
