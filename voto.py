
idade = int(input("Por favor, Digite sua idade: "))
print(idade)

if idade <= 15:
    print("Voto ainda não permitido!")

elif idade <= 18 >= 16:
    print("Voto faCUltatico!")

elif idade <= 70 >= 18 :
    print("Voto obrigatoria")

elif idade >= 70:
    print("Voto faCUltativo para pessoas acima de 70 anos")