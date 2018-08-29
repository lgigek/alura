print("********************************")
print("Bem vindo ao jogo de adivinhação")
print("********************************")

numero_secreto = 10

numero_usuario = int(input("Digite o seu número: "))
print("Você digitou o número", numero_usuario)

if (numero_secreto == numero_usuario):
    print("Você acertou")
else:
    print("Você errou")