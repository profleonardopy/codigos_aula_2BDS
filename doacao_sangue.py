idade = 30
peso = 55
gravida = False
doou_90_dias = False
if 16 <= idade <= 69 and peso >= 50 and not gravida and not doou_90_dias:
    print("Você está apto para doar sangue!")
else:
    print("Infelizmente, você não está apto para doar sangue.")
