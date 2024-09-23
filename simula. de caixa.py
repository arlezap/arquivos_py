import random

print('\n|Olá, digite seus dados de acesso para poder efetuar um saque no caixa 24 horas.|\n')

saldo = 1000
saque = 5
opção = 0

cpf = int(input('Digite seu CPF: '))
senha = int(input('Digite sua senha: '))

if (cpf == 123 and senha == 123):
    opção = 0
    
    while opção != 4:
        print('Olá, seja muito bem vindo a sua conta')
        print('(1) Extrato\n(2) Sacar\n(3) Depositar\n(4) Fechar')
        opção = int(input('Digite o que você deseja realizar: '))

        if (opção == 1):
            numero_conta = random.randint(1000,9999) 
            print('Número da conta:', numero_conta)
            print('Saldo: R$', saldo)
            print('Saques disponíveis:', saque)

        elif(opção == 2):
            saque_ok = int(input('Digite o valor que você deseja sacar: '))
            if(saque_ok <= saldo):
                saldo = saldo - saque_ok 
                print(f'Você sacou R${saque_ok} da sua conta.')
                print(f'Agora você tem R${saldo} disponível em conta.')
                saque = saque -1 
                print(f'Você só pode realizar mais {saque} saques da sua conta.')
            if(saque_ok >= saldo): 
                print('Você não tem esse valor disponível na conta!')

        elif(opção == 3):
            deposito = int(input('Digite o valor que você deseja depositar: '))
            saldo = deposito + saldo 
            print(f'Você depositou R${deposito} na sua conta com sucesso e ficou com R${saldo} disponível na conta!')    
