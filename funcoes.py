# Função simples que não recebe parâmetros nem retorna valores
def saudacao():
    print("Olá, mundo!")

# Função que recebe parâmetros
def saudacao_pessoal(nome):
    print(f"Olá, {nome}!")

# Função que retorna um valor
def soma(a, b):
    return a + b

# Função com parâmetros padrão
def saudacao_com_tempo(nome, periodo_do_dia="dia"):
    print(f"Bom {periodo_do_dia}, {nome}!")

# Função que utiliza argumentos variáveis
def soma_varios(*numeros):
    return sum(numeros)

# Testando as funções

# 1. Chamando a função simples
saudacao()

# 2. Chamando a função que recebe parâmetros
saudacao_pessoal("Maria")

# 3. Chamando a função que retorna um valor
resultado = soma(5, 3)
print(f"A soma de 5 e 3 é: {resultado}")

# 4. Chamando a função com parâmetros padrão
saudacao_com_tempo("João")
saudacao_com_tempo("João", "noite")

# 5. Chamando a função que utiliza argumentos variáveis
resultado_varios = soma_varios(1, 2, 3, 4, 5)
print(f"A soma de 1, 2, 3, 4 e 5 é: {resultado_varios}")
