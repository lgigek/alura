print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 10

numero_usuario = int(input("Digite o seu número: "))
print("Você digitou o número", numero_usuario)

acertou = numero_secreto == numero_usuario
eh_maior = numero_secreto < numero_usuario
eh_menor = numero_secreto > numero_usuario

if acertou:
    print("Você acertou!")
else:
    if eh_maior:
        print("Você errou! O seu chute foi maior que o número secreto.")
    elif eh_menor:
        print("Você errou! O seu chute foi menor que o número secreto.")
print("Fim do jogo")
