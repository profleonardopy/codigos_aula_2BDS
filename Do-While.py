# Inicializamos a variável 'continuar' como True para iniciar o loop
continuar = True

# Iniciamos um loop while que continuará até que 'continuar' seja False
while continuar:
    # Pedimos ao usuário para fornecer uma resposta (s/n)
    resposta = input("Deseja continuar? (s/n): ")
    # Verificamos se a resposta do usuário é 'n' (para sair do loop)
    if resposta.lower() == 'n':
        # Se a resposta for 'n', alteramos 'continuar' para False, encerrando o loop
        continuar = False
