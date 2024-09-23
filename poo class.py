class cat:

    def __init__(self, raça, cor, nome, sexo, peso, altura, data_nascimento, quantidade_comida_porção):
        self.raça = raça
        self.cor = cor
        self.nome = nome
        self.sexo = sexo
        self.peso = peso
        self.altura = altura
        self.data_nascimento = data_nascimento
        self.quantidade_comida_porção = quantidade_comida_porção
        self.comida = 1000

    def imprimir_informações(self):
        print(f'|--INFORMAÇÕES--|\n Nome: {self.nome}\n Raça: {self.raça}\n Cor: {self.cor}\n Sexo: {self.sexo}\n Peso: {self.peso}\n Altura: {self.altura}\n Data Nasc: {self.data_nascimento}\n Porção: {self.quantidade_comida_porção}\n Qnt Comida: {self.comida}')

    def comer(self):
        self.comida -= self.quantidade_comida_porção
        print(f'O cat {self.nome} ainda possui {self.comida} gramas.')


    def miar(self):
        print(f'O cat {self.nome} está miando!!')


if __name__ == '__main__':
    my_cat = cat('Esquilo', 'preto', 'Otto', 'Espada', 0.50, 0.60, '01/08/2023', 40)
    second_cat = cat('Siamês', 'Misto', 'Ozzu', 'Eu quero', 420, 69, '23/06/2024', 150)
    my_cat.miar()
    my_cat.comer()
    second_cat.miar()
    second_cat.comer()
    my_cat.imprimir_informações()
    second_cat.imprimir_informações()
    
    
    