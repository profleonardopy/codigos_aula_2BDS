#Definindo variável de controle
controle = 1
# enquanto a variável de controle for diferente de 0
# ele vai executar o có1digo
while controle != 0:
    #Entrada de dados (Número Inteiro) pelo usuário
    entrada = int(input("Digite um número inteiro:\n1 - Soma\n2 - Sair\n"))
    # Se a entrada = 1, executa o if
    if(entrada == 1):
        num1 = float(input("Primero número: "))
        num2 = float(input("Segundo número: "))
        resultado = num1 + num2
        print("O resultado da soma é: ",resultado)
    #Se entrada = 2 Executa o elif
    elif(entrada == 2):
        print("Saindo do programa!")
        controle = 0
    #Se entrada não estiver nas condições anteriores executa o else
    else:
        print("Entrada incorreta!\n.\n")
print(".\n.\n.\nFIM!")