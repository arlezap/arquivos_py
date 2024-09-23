for i in range(10):
    print(i)

nomes = ["ArlaeX", "Marli", "Arbusto", "LeandroLins", "Ander"]

for nome in nomes:
    print(nome)

valor = 99

while valor != "sair":
    valor = input("Digite um valor: ")
    if valor != "sair":
        valor = int(valor)