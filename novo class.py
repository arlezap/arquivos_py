class person:

    def __init__(self, nome='', cpf='', sexo='', ano_nascimento = 0, salario_bruto = 0.0):
        self.nome = nome
        self.cpf = cpf
        self.sexo = sexo
        self.ano_nascimento = ano_nascimento
        self.idade = self.calcular_idade()
        self.salario_bruto = salario_bruto
        self.salario_líquido = self.calcular_salario_líquido()

    def calcular_porcentagem(self, porcentagem):
        return (self.salario_bruto * porcentagem) / 100
    
    def calcular_salario_líquido(self):
        return self.salario_bruto - (self.calcular_desconto_inss() + self.calcular_desconto_irrf())
    
    def calcular_desconto_inss(self):
        salario = self.salario_bruto
        if salario <= 1412.00:
            return self.calcular_porcentagem(7.5)
        elif salario > 1412.00 and salario <= 2666.68:
            return self.calcular_porcentagem(9.0)
        elif salario > 2666.68 and salario <= 4000.03:
            return self.calcular_porcentagem(12.00)
        else:
            return self.calcular_porcentagem(14.00)

    def calcular_desconto_irrf(self):
        salario = self.salario_bruto
        if salario >= 2259.21 and salario <= 2826.65:
            return self.calcular_porcentagem(7.5)
        elif salario > 2826.65 and salario <= 3751.05:
            return self.calcular_porcentagem(15.00)
        elif salario > 3751.05 and salario <= 4664.68:
            return self.calcular_porcentagem(22.5)
        elif salario > 4664.68:
            return self.calcular_porcentagem(27.5)
        else:
            return

    def calcular_idade(self):
        return 2024 - self.ano_nascimento

    def imprimir_informações(self):
        print(f'|!--INFORMAÇÕES--!|\n Nome: {self.nome}\n CFP: {self.cpf}\n Sexo: {self.sexo}\n Data Nasc: {self.ano_nascimento}\n Salario Brut: {self.salario_bruto}\n Salario Liq: {self.salario_líquido}\n Idade: {self.idade}')

if __name__ == '__main__':
    #person_1 = person('Arle', '132.427.709-35', 'Sempre', 2004, 3256.00)
    #print(round(person_1.salario_líquido,2))
    person_2 = person()
    person_2.nome = input('Digite seu nome: ')
    person_2.cpf = input('Digite seu cpf: ')
    person_2.salario_bruto = float(input('Digite seu salario_bruto: '))
    person_2.ano_nascimento = int(input('Digite seu ano de nascimento: '))
    person_2.sexo = input('Digite seu sexo: ')
    person_2.salario_líquido = person_2.calcular_salario_líquido()
    person_2.idade = person_2.calcular_idade()
    person_2.imprimir_informações()
    
