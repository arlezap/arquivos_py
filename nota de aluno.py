"""
    Solicitar ao úsuario quatro notas de um aluno, e o seu nome, calcular a média e mostrar o nome e sua média.
"""
nome = input("Digite seu nome: ")

n_1 = float(input("Digite a primeira nota: "))
n_2 = float(input("Digite a segunda nota: "))
n_3 = float(input("Digite a terceira nota: "))
n_4 = float(input("Digite a quarta nota: "))
media = ((n_1 + n_2 + n_3 + n_4) / 4)

print(nome)
print(f"O Aluno: {nome} ficou com a media: {media}")

print(f"As notas do aluno foram: {n_1, n_2, n_3, n_4} e a média ficou: {media}")

if media >= 7.0:
    print(f"O aluno {nome} está aprovado!! >_<")

elif media >= 5.0:
    print(f"O aluno {nome} está em recuperação! xD")

else:
    print(f"O aluno {nome} está reprovado")

